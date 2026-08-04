# Finding an Outdated Git Mirror Host

## Summary
When dealing with Git repositories backed by multiple IP addresses (such as load-balanced mirrors), `git fetch` offers minimal control over network-level routing if a specific mirror goes out of sync or fails. This guide demonstrates a quick, practical technique to query individual backend servers directly by leveraging the Git HTTP protocol and `curl`'s `--resolve` option, helping you pinpoint and isolate outdated mirror hosts.

---

## The Problem
Suppose you have a Git repository backed by several distinct hosts (for example, the multiple IP addresses behind `https.git.savannah.gnu.org`), and one of them appears to be outdated or malfunctioning. 

Git itself provides very few tools to examine or control which specific host or IP address the fetching process uses. The best `git fetch` can do is restrict communication to IPv4 or IPv6 addresses. Because `git fetch` prioritizes Git-level verbosity over network diagnostics, it assumes the underlying network will "just work."

## The Solution: Querying via the Git HTTP Protocol
We can bypass standard Git routing by taking advantage of the [simple Git HTTP protocol](https://git-scm.com/docs/http-protocol) to query every server individually. 

Specifically, we can use [dumb client reference discovery](https://git-scm.com/docs/http-protocol#_dumb_clients) to inspect the commit ID of specific references (like branch heads) on each server. To target a specific IP address behind an HTTPS domain name, we use [`curl`'s `--resolve` option](https://curl.se/docs/manpage.html#--resolve), which maps a server name to a specific IP address.

### Example Script

Here is a quick shell script to check the state of the `master` branch across all associated IPv4 and IPv6 addresses for a given host:

```bash
host=https.git.savannah.gnu.org
url=https://$host/git/emacs.git/info/refs
ipv4=$(dig +short a $host.)

# Curl requires IPv6 addresses to be formatted as '[...]'.
ipv6=$(dig +short aaaa $host. |
       sed -e 's/^/[/' -e 's/$/]/')

for i in $ipv4 $ipv6; do
  echo $i:
  curl -sS -L --resolve $host:443:$i $url |
    grep refs/heads/master
done
```

*(Note: `dig +short` is used here as a convenient way to retrieve raw IPv4 and IPv6 addresses.)*

## Analyzing the Results
Running this script allows you to see if all IP addresses are responding and whether any particular address is returning an old commit ID for `refs/heads/master`. 

### Next Steps & Potential Improvements
* **Script Automation:** You could enhance this script to automatically read the current HEAD commit from a local repository and flag only those mirrors that deviate from it.
* **Mitigation:** Since Git doesn't natively allow you to blacklist a single problematic IP address, dealing with a faulty mirror usually requires system-level intervention (such as blocking connections to that specific IP). As a temporary workaround, forcing IPv4 via `git fetch -4` can often bypass a broken IPv6 mirror.
* **Monitoring:** Mirror administrators can adapt this approach to continuously monitor backend synchronization and detect persistently lagging nodes.

***

*(Source: [Original Blog Post](https://utcc.utoronto.ca/~cks/space/blog/programming/GitFindingOutdatedMirrorHost) | [2 Comments](https://utcc.utoronto.ca/~cks/space/blog/programming/GitFindingOutdatedMirrorHost?showcomments#comments))*