# Google Calendar "Unable to launch event" — Caused by Missing DTSTAMP

## Summary
For years, users have encountered the frustrating **"Unable to launch event"** error when trying to import certain `.ics` calendar attachments into Google Calendar on Android. After analyzing multiple broken invites using an [iCal validator](https://icalendar.org/validator.html), the root cause is clear: **a missing `DTSTAMP` property**, which is strictly required by the iCalendar specification (RFC 5545). This article explains how to identify the issue and fix the `.ics` file so Google Calendar can successfully import it.

---

## The Problem
When attempting to open specific email calendar attachments, Google Calendar throws an Android toast error message:

> *Unable to launch event*

*(Note: While these non-compliant files often work fine on iOS devices and some alternative Android calendars, they consistently fail on Google Calendar.)*

### Example of a Broken `.ics` File
Testing broken invites reveals a missing `DTSTAMP` property:

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:abcdef-ghij-klmn-opqrs-tuvwxyz
BEGIN:VEVENT
DTSTART:20260713T093000Z
DTEND:20260713T103000Z
SUMMARY:Your Delivery (Order 123456789)
UID:83c510fa-1be4-48a2-8338-c5a2350ba6e5
END:VEVENT
END:VCALENDAR
```

According to the [official iCalendar specification (RFC 5545)](https://www.rfc-editor.org/info/rfc5545/):
> **Property Name:** `DTSTAMP`  
> **Conformance:** This property **MUST** be included in the "VEVENT", "VTODO", "VJOURNAL", or "VFREEBUSY" calendar components.

---

## The Solution
To fix the file, simply insert the `DTSTAMP` property (typically matching the start time or current timestamp) into the `VEVENT` block.

### Example of a Working `.ics` File
```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:abcdef-ghij-klmn-opqrs-tuvwxyz
BEGIN:VEVENT
DTSTAMP:20260713T093000Z
DTSTART:20260713T093000Z
DTEND:20260713T103000Z
SUMMARY:Your Delivery (Order 123456789)
UID:83c510fa-1be4-48a2-8338-c5a2350ba6e5
END:VEVENT
END:VCALENDAR
```

You can download and test both versions to see the behavior firsthand:
* [Broken calendar invite](https://shkspr.mobi/blog/wp-content/uploads/2026/07/broken.ics)
* [Working calendar invite](https://shkspr.mobi/blog/wp-content/uploads/2026/07/working.ics)

---

## The Documentation Gap
While the iCalendar spec is well-defined, [Google's official documentation on iCal files](https://support.google.com/calendar/answer/37118?#zippy=%2Ccreate-or-edit-an-icalendar-file) is frustratingly vague. It lists the outer wrapper:

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:<[enter ID information here]>
BEGIN:VEVENT
(event details)
END:VEVENT
END:VCALENDAR
```
...but it never actually describes what those required "event details" are. 

## Final Thoughts
Is the iCalendar specification needlessly verbose? Perhaps. Should Google Calendar be more forgiving of non-compliant inputs? Probably! 

Since there is no straightforward way to file a bug report directly with Google's product teams, the best workaround for now is to notify the organizations sending these broken invites and request that they update their generation systems.