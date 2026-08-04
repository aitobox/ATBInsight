# Making Sense of Diskless Workstations Through Two Models

## Summary
When examining the history of early Unix diskless workstations (such as early SunOS setups), a common question arises: *Was the massive performance bottleneck of multiple users sharing a single hard drive over a slow network ever truly worth it?* 

While economic ROI calculations often faltered in environments like university labs, the true value of diskless workstations becomes clear when viewed through two distinct usage models: **the inferior substitute for a local disk** and **the superior replacement for a serial terminal**. These two paradigms altered how organizations weighed hardware costs against user productivity, ultimately shaping the adoption of early networked computing.

---

## 1. The Question of Value and ROI
When I previously wrote about [how early SunOS handled diskless workstations](https://utcc.utoronto.ca/~cks/space/blog/solaris/SunOSDisklessWithoutNFS), a reader raised a valid point:

> *"Obviously this is slow, but having an indeterminate number of users sharing a circa 1982 mechanical hard drive sounds like a problematic amount of slow. Was this ever truly worth doing? I know hard drives were wildly expensive back then, but surely the work slowdown from having multiple users sharing a single hard drive in this fashion would mean the ROI for those hard drives would seem obvious?"*

While some deployment environments—such as university graduate student terminal rooms—did not operate on strict corporate "ROI" metrics, a deeper examination reveals that diskless workstations served two entirely different conceptual roles.

---

## 2. Model 1: The Inferior Substitute for a Local Disk
In the first model, a diskless workstation was viewed simply as a cost-saving, yet strictly inferior, alternative to a workstation equipped with a local disk. 

* **The Trade-off:** You saved money on expensive local hardware (and potentially bought a lower-end base model, like the Sun 3/50 instead of the faster 3/60). 
* **The Cost:** Performance suffered significantly due to disk I/O bottlenecks across a shared 10MBit network connected to a central server with mechanical HDDs shared by multiple users.
* **The Dynamics:** This setup was typically reserved for users whose productivity was valued less. Consequently, workstations with local disks naturally became status symbols, marking employees important enough to justify the extra hardware expense.

---

## 3. Model 2: The Superior Replacement for a Serial Terminal
In the second model, a diskless workstation was not a downgrade from a local disk, but rather a massive upgrade from a traditional serial terminal—much like [X terminals](https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate) were later on.

* **The Advantages:** Instead of a single text-only window with zero local computing power, users gained access to multiple windows, graphical interfaces, and local compute capabilities that often outpaced an overloaded central server. 
* **The Economics:** While diskless workstations were significantly more expensive than serial terminals, organizations could potentially save money on the central server because it no longer needed massive compute capacity to handle direct logins from everyone.
* **The "Personal Computer" Model:** Crucially, unlike fixed terminal networks, this model [lent itself well to incremental upgrades](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/FundingAndHardwareSize). Organizations could replace units with better workstations (potentially with local disks) one by one, shifting from a rigid "terminal" model to a flexible ["personal computer" model](https://utcc.utoronto.ca/~cks/space/blog/tech/ScalingTerminalsVsPCs).

---

## 4. Cost-Benefit Divergence
These two opposing models led to entirely different calculations of cost and benefit:

* **Model 1 (Downgrade):** You trade productivity for hardware savings. The primary question is whether the lost productivity outweighs the money saved.
* **Model 2 (Upgrade):** You invest more in hardware to gain user productivity. The question is whether the productivity boost outweighs the higher cost of diskless hardware compared to serial terminals (factored alongside potential savings on central servers and serial lines). 

Eventually, these models began to overlap, creating a complex spectrum involving serial terminals, diskless workstations, and local-disk workstations tailored to different user groups. The introduction of NFS and shared, writable filesystems further blurred the lines, allowing even "local disk" workstations to NFS-mount home directories and shared workspaces to facilitate collaboration.

Later, [X terminals](https://utcc.utoronto.ca/~cks/space/blog/unix/XTerminalsNotImmediate) inserted themselves into this spectrum by offering graphics without local computation—a configuration that appealed to users who needed graphical environments, but preferred to keep heavy compute tasks on the same machine holding their data on HDDs rather than shuttling it over shared 10MBit networks.

---

## 5. The Commercial Strategy
Beyond technical models, there was a clear commercial incentive for vendors. Early Unix workstation manufacturers like Sun were eager to gain a foothold in new markets where Unix was still an unproven commodity. 

By offering a low-cost, entry-level diskless configuration alongside a compatible server, vendors could get their foot in the door with budget-conscious companies. Once organizations got a taste of Unix, vendors could upsell them to faster, more expensive hardware down the line. (Sun notably continued this strategy later by selling entry-level hardware lacking onboard floating-point units.)

***

*Source: [Original post and discussion comments](https://utcc.utoronto.ca/~cks/space/blog/tech/DisklessWorkstationsTwoModels).*