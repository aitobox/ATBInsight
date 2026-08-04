# Presigned URLs are technically a security vuln

> **Summary:** 
> Replayable auth tokens are typically viewed as a textbook security vulnerability, yet object storage systems like Tigris use them deliberately as a first-class feature: **presigned URLs**. By examining how Amazon’s SigV4 protocol prevents replay attacks using the system clock, we can understand how presigned URLs turn this limitation into a powerful, stateless capability grant—at the cost of revocability and leak risks.

---

## Replay attacks are a real problem and the classic fix is miserable

When you authenticate a request with Amazon's SigV4 protocol for Tigris, your client boils down the request to a canonical form: a SHA256 hash of the request's method, path, query parameters, signed headers, and a SHA256 hash of the payload. It runs the result of that through HMAC with a signing key derived from your secret access key. Nothing secret ever crosses the wire. The server derives the same key as the client, does the same canonical form transformation, and compares the result.

Being able to make a valid signature proves that the request came from someone holding the secret access key, but it proves nothing about *when* that request was made. A signature that was made a year ago would still be valid today, so in theory an attacker could warehouse your signed requests only to replay them en masse later. Imagine sitting on a pile of signed "create EC2 instance" calls only to spam them all out at a later date. You would be a twirling mustache villain able to spawn dozens of servers at a moment's notice.

Traditionally the fix is to bake a nonce (number used once) into the signature. This makes every signature differ because that nonce differs.

However, with great power comes great responsibility, and making sure that something used once is only used once is a surprisingly hard distributed systems problem. You can't verify that something is only used once locally. Say you store them all for a 15-minute smear window at a low request rate like 10,000 Bq. That's 9 million live nonces, and every frontend node needs to have a consistent view of the whole set as it churns.

You have made your fast authentication check slow from having to ensure things are only used once.

What you want instead is something that changes constantly without coordination and invalidates those old signatures for free. For an added bonus, you want this to also be in the standard library of every programming language.

---

## Sign the clock

There's exactly one value that changes constantly, (mostly) monotonically, and is already actively coordinated across all elements of the stack: **the clock**. 

Your OS already keeps time in sync with the public NTP pool (or a private NTP pool if you are cool enough to have radioactive PCI cards laying around). Without an accurate view of time you can't make TLS connections, which means you can't make API calls to Tigris at all, so the auth layer gets to assume a working clock exists.

SigV4 signs the current time into the request. If an attacker gets their greasy hacker paws on a signature, they have about 15 minutes to use it before it becomes a digital paperweight. If time is an input to the signature and the time changes enough to invalidate the signature, the signature is null and void. Sure, in theory a sufficiently funded attacker could create a black hole in your datacenter and disrupt temporal flow, but at that point the planet is probably toast, which makes the attack profile moot. Commit mass object storage fraud with this one neat trick!

This makes your verification stay stateless. Everything gets checked against the system clock the server already needs, and you can give clients a 15-minute signature smear window as a grace period for old or delayed clients (exponential backoff is a good thing and Tigris will reward you for doing it).

Of course, the real thing keeping the signatures safe on the wire is TLS (HTTPS). If that is broken we have bigger problems and object storage fraud is the least of our worries.

Time is the only nonce you need because both sides already agree on it anyway.

---

## Some thorns have roses

Presigned URLs take the replay tolerance that SigV4 spends all this effort nerfing and buffs it into a feature. The entire auth dance gets flattened into URL parameters that any HTTP client can use, be it a browser, `curl`, Go's `net/http`, or something you made by bit-banging HTTP over a socket. 

Here's a real presigned URL:

```http
https://xe-sophia-base.t3.tigrisfiles.io/moby-dick.txt
?X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=tid_ubYBNEYAmTciLVwszw_QrUXDmtcyQisryryGfxgznDsCnOvNqh/20260714/auto/s3/aws4_request
&X-Amz-Date=20260714T043308Z
&X-Amz-Expires=3600
&X-Amz-SignedHeaders=host
&X-Amz-Signature=0dcaf4972911527a7582ff36ea457e9760a8efccb6655a178685aaa281637a36
```

### Anatomy of a Presigned URL

* **`X-Amz-Algorithm`**: The signature scheme. Effectively always `AWS4-HMAC-SHA256`.
* **`X-Amz-Credential`**: The access key ID plus the credential scope — date, region, service, and the literal terminator `aws4_request`. The signing key is derived by chaining HMAC through exactly those parts, so a signature is only ever valid for that day, that region, that service.
* **`X-Amz-Date`**: The second the URL was born, in UTC.
* **`X-Amz-Expires`**: How many seconds it gets to live, chosen by the signer.
* **`X-Amz-SignedHeaders`**: Which HTTP headers are folded into the signature. Usually just `host`, because you can't force whoever you hand a URL to into sending exotic headers.
* **`X-Amz-Signature`**: 64 hex characters of HMAC-SHA256 over the canonical request — the method, the path, every parameter above, the signed headers, and the payload hash. Change any of them and the math stops agreeing.

All of these are normally HTTP headers in standard SigV4 requests:

```http
GET /moby-dick.txt HTTP/1.1
Host: xe-sophia-base.t3.tigrisfiles.io
X-Amz-Date: 20260714T043308Z
X-Amz-Content-Sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Authorization: AWS4-HMAC-SHA256 Credential=tid_ubYBNEYAmTciLVwszw_QrUXDmtcyQisryryGfxgznDsCnOvNqh/20260714/auto/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=0dcaf4972911527a7582ff36ea457e9760a8efccb6655a178685aaa281637a36
```
*(Note: This request is an example to illustrate the point, here be dragons, etc.)*

It's best to think about this presigned URL as a **capability grant**. Whoever holds it gets to make exactly one (1) kind of API call with one (1) HTTP method against one (1) object in one (1) bucket. They can do this as many times as they want until the presigned URL expires. The signature covers the method, the path, and the signed headers so a user can't take a presigned request for `GET`ting a copy of *Moby Dick* from a development environment and weaponize it into a way to delete everything in your production bucket.

Possession is authorization until the clock says no.

---

## What it costs you

Capability grants like this can have some sharp edges:

* **No granular revocation:** There is no real way to revoke any individual presigned URL short of killing the access key it was signed with. When that key dies, everything it signed dies too. 
* **Expiry limits:** A presigned request can live anywhere from one (1) second to one (1) week (seven periods of twenty-four hours).
* **Unlimited usage within the window:** There's no limit to the number of times a client can use a presigned request. If you give a mouse permission to `GET` one cookie, they can `GET` that same cookie over and over. You end up having to pay for the `GetObject` calls in the end.
* **Leak vectors:** URLs leak. Presigned URLs will end up in API responses, chat messages, GitHub comments, and your browser history. The tradeoff is acceptable because all the links self-destruct, but it's a tradeoff you need to keep in mind when you design your services.

Presigned URLs sound like a great way to prevent hotlinking. At some level they are, but what they actually do is put a *lifetime* on hotlinking, making things annoying enough that it usually gets people to stop.

---

## The hole in the fence is the gate

SigV4 makes a lot of API authentication challenges much easier. It spent most of its innovation budget on making signatures die quickly because replay attacks are the classic way that signed requests go wrong. Presigned URLs looked at that property, shrugged, flipped it on its head, and made it into a feature.

The thing that looked like a problem becomes a fundamental construct to build your apps upon.

Want to hand out links that expire themselves? Tigris supports presigned URLs out of the box with the same SigV4 dance you already know, on globally distributed, S3-compatible object storage. 

👉 **[Read the Tigris Docs](https://www.tigrisdata.com/docs/objects/presigned/)**