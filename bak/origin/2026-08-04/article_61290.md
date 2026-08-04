# Firefox in WebAssembly

> **Summary:** Puter has successfully compiled Firefox to WebAssembly, making it possible to run an entire web browser directly inside another browser. Powered by AI-assisted development and advanced networking protocols, this remarkable technical feat opens up new possibilities for client-side virtualization—while presenting unique infrastructure challenges.

---

## Overview

In what can only be described as an absurdly cool technical achievement, [Puter](https://developer.puter.com/labs/firefox-wasm/) has compiled Firefox into WebAssembly (WASM). This allows you to run the full Firefox browser natively inside another browser, such as Google Chrome.

![A Chrome window showing the Firefox UI running inside a tab. The Chrome network panel on the right displays loaded resources, including a 233MB `gecko.wasm` file and an 18MB `chrome-assets.tar.zst` archive.](http://localhost/proxy/tnG0A7-qydBW4-M81dnNshmtX5FWlrAJvZ3udw8Dlyo=/aHR0cHM6Ly9zdGF0aWMuc2ltb253aWxsaXNvbi5uZXQvc3RhdGljLzIwMjYvZmlyZWZox3dhc20ud2VicA==)

## Engineering Highlights

* **Why Firefox?** The team chose Firefox/Gecko because of its robust single-process support.
* **AI-Assisted Development:** The project utilized an estimated $25,000 worth of Claude Opus and Fable tokens. However, by leveraging a Claude Max subscription plan, the actual out-of-pocket cost was significantly lower.
* **Network Routing:** Because standard browser environments restrict arbitrary network connections, the demo funnels all traffic through Puter's servers using the [Wisp protocol](https://github.com/MercuryWorkshop/wisp-protocol) over WebSockets. 
* **Infrastructure Scaling:** Proxying this volume of traffic is resource-intensive; the team [had to actively scale up their servers](https://news.ycombinator.com/item?id=48926939#48936563) to handle the surge in traffic during the project's Hacker News discussion.
* **End-to-End Encryption:** Puter claims the setup supports end-to-end encryption. Inspection of the WebSocket traffic confirms that requests to HTTPS sites remain encrypted, while legacy HTTP traffic (such as `http://www.example.com/`) appears in cleartext.

---

## Resources & Related Projects

* **Source Code:** Check out the official [`firefox-wasm` repository](https://github.com/HeyPuter/firefox-wasm) on GitHub.
* **Alternative Approaches:** [theogbob/WebkitWasm](https://github.com/theogbob/WebkitWasm) is a similar experimental project compiling WebKit to WASM, though it does not currently feature a public online demo.

---

*Via [Hacker News](https://news.ycombinator.com/item?id=48926939)*

**Tags:** [browsers](https://simonwillison.net/tags/browsers), [firefox](https://simonwillison.net/tags/firefox), [ai](https://simonwillison.net/tags/ai), [webassembly](https://simonwillison.net/tags/webassembly), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [ai-assisted-programming](https://simonwillison.net/tags/ai-assisted-programming), [claude](https://simonwillison.net/tags/claude), [claude-mythos-fable](https://simonwillison.net/tags/claude-mythos-fable)