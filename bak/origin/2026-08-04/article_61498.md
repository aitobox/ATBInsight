# OpenAI Starts Cleaning Up the Utter Mess It Made of ChatGPT

> **Summary:** OpenAI is rolling out updates to fix the chaotic initial launch of its redesigned ChatGPT desktop app, addressing missing features like cross-device history syncing and confusing mode navigation. However, critics argue the software remains bloated, and the confusing transition between the new app and newly rebranded "ChatGPT Classic" rivals the infamous "New Coke" marketing blunder.

---

## Fixing the Incoherence

Thibault “Tibo” Sottiaux, the OpenAI engineering lead spearheading the desktop app, shared the company's response to early criticism on X (formerly Twitter):

> Evening! We’ve gotten lots of great feedback on the new ChatGPT desktop app (which we didn’t get totally quite right on the first try), and as a result, we’ve made some changes.
> 
> 1/ ChatGPT conversation history and projects are now visible in the sidebar. Also, your Chat and Work history now sync across web, mobile, and desktop. Local tasks still stay on your computer.

*How in the world did they ship this without sync in the first place?* Sottiaux continued:

> 2/ You can now easily switch between Chat and Work modes inside ChatGPT on desktop, which is now also consistent with how it shows on web and mobile.

Bringing back “chat” to ChatGPT is literally the least they could do. Hiding chat in an obscure corner of the interface from an app explicitly named “ChatGPT” is akin to removing text editing from an app called TextEdit.

---

## Still a Bloated Experience

While the recent updates address some of the [abject incoherence of the initial rollout](https://daringfireball.net/linked/2026/07/11/can-someone-explain-to-me-how-to-get-chatgpt-classic), the app remains heavily criticized as a 1.5 GB Electron monstrosity. (Or, if it isn't technically Electron, it's because OpenAI built [another bloated layer of abstraction around it](https://openai.com/index/building-chatgpt-atlas/). Sottiaux seemingly oversees the only engineering group that looked at Electron and decided it was too slim and close to the metal.)

---

## The "ChatGPT Classic" Update Confusion

The software update dialog in the older version of the app—now officially renamed **ChatGPT Classic**—has proven equally baffling. 

> [![Screenshot of the last pre-“Classic” ChatGPT app’s Check for Updates dialog, with confusing instructions.](http://localhost/proxy/Qzv9lpYKGdy0w9LG7baFND7t5sDK961mGlJt1QAbWUg=/aHR0cHM6Ly9kYXJpbmdmaXJlYmFsbC5uZXQvbWlzYy8yMDI2LzA3L2NoYXRncHQtdXBkYXRlcy5wbmc=)](https://daringfireball.net/misc/2026/07/chatgpt-updates.png)

Essentially, if you have ever installed the *new* ChatGPT, clicking the “Install Update” button in this dialog does nothing—aside from taking a moment to quietly quit the application. 

If you've never touched the new app, the dialog successfully updates the legacy software to the latest version of *ChatGPT Classic*. But if you've already tried the new version and want to revert, you are forced to [download and install ChatGPT Classic manually](https://persistent.oaistatic.com/sidekick/public/ChatGPT_Classic.pkg), even while looking at an active update prompt inside the legacy app.

Ultimately, this entire rollout makes the [“New Coke” / “Coke Classic” fiasco](https://en.wikipedia.org/wiki/New_Coke) of the 1980s look like a masterclass in strategic product management.

---

*[★ Permanent link to the original article on Daring Fireball](https://daringfireball.net/linked/2026/07/17/openai-chatgpt-mess)*