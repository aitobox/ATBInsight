# Mandatory Update: A Short Story

### Summary
*Mandatory Update* is a fictional narrative centered on Nyx-Ø Linwood, a DevOps engineer who attends DEF CON 34. While grappling with her mother’s ongoing legal battle against a tech billionaire, Nyx discovers her own agency through the world of hacking. The story explores themes of self-determination, the ethics of digital security, and the power of technical skill to dismantle systemic abuse.

---

## The Setup
My name is Nyx-Ø Linwood, and I hate it. Not "Nyx." That part's fine. It's the Ø, the pretentious little circle with a line through it that my father insisted on because he thinks he's a fucking visionary. 

I'm sitting at our kitchen table in our cramped San Francisco apartment. My mom, Lyra Linwood, is fighting the same fight she has been since I was born. She was Jared Vane's 19-year-old employee when the then-billionaire got her pregnant. He lost custody after a years-long legal fight, but it left her dealing with an army of Jared stans trolling her. Thanks to SlopstreamAI (Jared's newest company), it's much worse. Her trolls use Slopstream to generate noncon deepfake nudes of her. So she's suing Slopstream and Jared, again. But it's not going well.

"You just focus on that big conference you're going to," Mom says.

I open the HackerTracker app on my phone, scrolling through the DEF CON schedule. I've never been to DEF CON before. I don't know anyone who will be there, and as a woman in a male-dominated field, I probably don't even belong, anyway.

---

## Arrival at DEF CON
Thursday morning. Inside the air-conditioned Las Vegas Convention Center, DEF CON is lit. I wait in the registration line with hundreds of people. When I finally get to the front, they hand me a custom circuit board—my conference badge.

I wander the halls, eventually finding the Bug Bounty Village. I meet Jade, a woman with bright, colorful hair. 

"You *just* do DevOps?" she says, incredulous. "You mean, you just orchestrate thousands of computers, bending them to your will, with a single command? Girl, you have a *superpower*."

I never thought of DevOps like that. Issuing a command on my laptop to bend an army of servers to my will. *Slay.*

---

## The Target
It's not until I wander into the Car Hacking Village that I'm snapped back into my shitty reality. Next to a 10-foot-tall banner is an actual Volta Model Z. Volta, the biggest and most profitable EV company in the country, *and* the biggest source of my father's obscene wealth.

I meet Julian Cross, the Vice President of Engineering Infrastructure at Volta. He’s an arrogant prick who talks down to me. On a whim, I switch my WiFi device to monitor mode and open Wireshark. I pop a shell on his laptop, and now I can browse his filesystem. I capture the biggest flag of my entire fucking life.

---

## The Breach
I spend the night in my hotel room, deep in exploration. I’m logged into the VP of Engineering's GitHub account. He has access to *everything*. I clone a copy of every single repo—there are hundreds of them. I focus on the GitHub Actions workflows. This is the automation, how the software gets deployed. This is DevOps: my specialty.

I drift off to sleep, feeling powerful for the first time in my life.

---

## The Vulnerability
Saturday, late morning. I head to the Car Hacking Village. I’ve been focusing my Volta research on the infotainment system. I find a critical vulnerability: the update mechanism extracts firmware *before* verifying the digital signature. If the version number stays the same, it skips the verification entirely.

I text Jade: "I think I just found a critical vuln in Volta's update mechanism. The max payout is $100k!!!"

But then, the news hits. Jared Vane is going psycho on his baby mama, my mom, on social media. He's posting screenshots of her private text messages. The law can't stop him. Money can't stop him. You know who *can* stop him? *Me.*

Fuck the bug bounty. I'm going to burn Volta to the ground.

---

## The Payload
I spend the next several hours writing malware. I need to get Julian's Yubikey to sign a malicious git tag. I find him at a party at the Mandalay Bay. After a clumsy "accident" involving a spilled beer, I swipe his Yubikey. 

I use his phone's passcode (which I recorded him typing earlier) to unlock the Yubikey. I push my commit to GitHub.

---

## The Aftermath
It's Sunday morning, and every single Volta in the world, all nine million of them, are *bricked*. 

When the infotainment system boots, it shows an image of an email—a real one from Jared Vane to Jeffrey Epstein. 

A week later, Mom is looking more relaxed than I've seen her in years. "Jared is offering a settlement," she says. "He's dropping everything."

I smile. "That's wonderful, Mom."

I open my laptop and get to work. I've got a spreadsheet full of oligarchs. There are still a lot of billionaires. I've got a lot of work to do.

---

***Author's Note:** To give credit where credit is due, the email from Jared Vane to Jeffrey Epstein is an actual real email written by Elon Musk and sent to Epstein on Christmas Day. The story draws inspiration from various public controversies surrounding the billionaire's personal and professional life.*