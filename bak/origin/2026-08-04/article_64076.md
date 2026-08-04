# Read This Before You Buy That TV Streaming Stick

## Summary
Security experts have long warned about generic TV streaming boxes that secretly rent out users' internet connections as residential proxies. However, new research from Bitsight reveals a darker reality: these cheap, off-brand devices are also weaponized in massive, automated ad fraud networks. Masquerading as mobile phones, tens of thousands of H96 streaming sticks are covertly clicking on ads across AI-generated websites, generating an estimated $50,000+ a day for a mainland China-based entity known as the Fengwo Group.

---

## The Anatomy of an Ad Fraud Network

Security researchers at Bitsight recently investigated a popular brand of generic streaming devices known as **H96**. Threat researcher **Pedro Falé** gained deep visibility into the operation after registering an expired domain previously used for device telemetry.

Instead of receiving standard TV box data, the domain was flooded with telemetry claiming that tens of thousands of H96 streaming sticks plugged into television sets globally were actually mobile phones made by manufacturers like Samsung, Vivo, Huawei, and Xiaomi. 

```
[H96 Streaming Stick] ---> (Spoofs Mobile Device) ---> [AI-Generated Websites] ---> [Automated Ad Clicks / Fraud]
```

Further investigation revealed that all infected devices shared two pre-installed apps tied to **Zhejiang Fengwo IoT Technology Ltd** (operating as the **Fengwo Group**). These apps orchestrate the ad fraud network by using the captive TV boxes to click on ads hosted on AI-generated websites featuring machine-generated news and blogs. Notably, these ads only appeared when visited by a device matching the spoofed mobile profile of an H96 stick.

---

## AI Digital Humans and Low-Skilled Operations

The primary domain for the Fengwo Group (`fwgcloud[.]com`) claims the company specializes in "AI digital humans" for customer service and companionship. However, behind this facade lies an industrial-grade ad fraud machine. 

Bitsight discovered that the Fengwo Group uses a proprietary implementation of Google’s **Blockly**—a visual programming language originally designed for children—to build its sham websites and automation scripts. 
* **Cost Efficiency:** By using Blockly, low-skilled operators can drag and drop code blocks to define fraud routines without needing deep technical expertise.
* **Human-Like Interaction:** To ensure the bots successfully navigate and click ads, the Fengwo Group integrates vision and reasoning systems that mimic human browsing behavior, silently launching browsers, managing tabs, and interacting with landing pages.

---

## TV On vs. TV Off: Proxy by Day, Fraud by Night

Bitsight's analysis uncovered a clever operational duality within the H96 devices:
* **TV On (HDMI Signal Detected):** The device functions as a **residential proxy**, renting the user's internet bandwidth to anonymous third parties (ranging from web-scrapers to cybercriminals).
* **TV Off:** The device switches gears to execute resource-intensive **ad fraud tasks**, ensuring the background malicious activity doesn't interfere with the user's video streaming experience.

Despite repeated warnings from the FBI and cybersecurity agencies, major e-commerce platforms like Amazon, Best Buy, and Newegg continue to market and sell hundreds of these insecure, uncertified Android-based devices. 

---

## The Scale of the Operation

* **Global Footprint:** Bitsight tracked approximately **38,000 TV boxes** phoning home to just one expired Fengwo Group domain.
* **Daily Revenue:** Conservative estimates suggest the ad fraud network generates close to **$50,000 per day**, excluding additional profits from the residential proxy side of the business.
* **Unresponsive Operators:** When KrebsOnSecurity attempted to reach out to the Fengwo Group for comment, the inquiry bounced back with a full inbox notification, signaling the sheer volume of traffic hitting their infrastructure.

---

## How to Protect Yourself

To safeguard your home network and personal data from being exploited by botnets and ad fraud syndicates:
1. **Stick to Name Brands:** Only purchase streaming devices from reputable manufacturers (e.g., Google TV, Apple TV, Amazon Fire Stick, Roku) that feature official OS builds and security certifications. You can verify official Android TV OS and Play Protect status using [Google's official instructions](https://support.google.com/googleplay/answer/7165974).
2. **Audit Your Apps:** Be extremely selective about the apps you sideload or install on smart TVs and streaming sticks, as many can bundle hidden proxy software.
3. **Check Threat Intelligence Lists:** Security firm Synthient maintains a [publicly accessible list of IoT products](https://github.com/synthient/public-research/blob/main/2026/01/kimwolf/product_names.csv) known to ship with pre-installed malicious applications and residential proxies (including certain generic digital photo frames and streaming boxes).