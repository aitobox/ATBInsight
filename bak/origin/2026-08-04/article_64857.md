# The Information on Apple’s Unusual Use of iCloud for Confidential Work

## Summary
Apple encourages new employees to use their personal Apple IDs for work-related iCloud storage during onboarding to avoid the inconvenience of carrying two phones. While Apple revokes access to official work directories upon departure, files shared outside these designated folders often remain accessible in former employees' personal iCloud accounts. This architecture stems from Apple's identity model, where a single Apple ID can manage multiple email addresses. Although *The Information* linked this practice to a trade secret lawsuit, Apple maintains that the case involves deliberate theft of unreleased technology rather than documents left behind in personal iCloud storage.

---

## The Onboarding and Offboarding Dilemma

When new employees join Apple, they are issued an iPhone and a Mac alongside an iCloud account with high storage capacity. During onboarding, Apple encourages hires to use their preexisting personal Apple IDs with this account to facilitate document sharing among co-workers. 

This policy addresses a practical limitation: iOS devices only allow users to log into one primary Apple ID at a time. Because carrying two phones is inconvenient for separating work and personal tasks, most employees choose to use their personal Apple IDs.

However, the offboarding process has blind spots:
* **Revoked Access:** When an employee leaves, Apple revokes access to the dedicated "Apple Work" folder and internal authentication systems (like Slack).
* **Retained Files:** Because employees use personal iCloud accounts, any confidential files stored *outside* the managed work directory remain accessible after departure.

## The Nuance of Apple ID Architecture

Unlike traditional corporate accounts tied strictly to a single work email, an Apple ID is a persistent account capable of linking multiple email addresses (e.g., `example@icloud.com`, `example@gmail.com`, and a work address like `example@apple.com`). 

When an employee departs, they lose access to their `@apple.com` address, but the broader Apple ID account—representing the person rather than a single corporate inbox—remains intact. Even if an associated email address is later deleted, access to items shared with the overarching Apple ID persists. This humane approach to digital identity inherently makes corporate access restrictions much more complex than the standard "one email equals one account" model used by most businesses.

## Apple’s Response to the Controversy

Reports highlighting this iCloud workflow have been tied to Apple's legal actions against former employees or external entities, such as OpenAI. However, Apple issued a clear rebuttal to *The Information*:

> "This case is about OpenAI employees wrongfully taking Apple’s secret and confidential information regarding our unreleased technologies, processes, and products. Nothing in the filing relates to documents shared by, or stored in, iCloud."

Apple further clarified that it does not pursue legal action against former employees who merely retain leftover Apple documents in their personal iCloud accounts by accident.

---

*[Permanent Link to Original Article](https://daringfireball.net/linked/2026/08/03/the-information-apple-employees-icloud)*