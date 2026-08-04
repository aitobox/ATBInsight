# How Early SunOS Did Diskless Workstations Before NFS

## Summary
Before the invention of NFS, early SunOS workstations relied on a block-level network disk protocol called **`nd`** to boot and operate without local disks. While network-attached block storage isn't inherently unusual, SunOS `nd` was notoriously "cursed." It required administrators to manually carve up raw disk sectors into custom subpartitions with zero sanity checking, operated entirely over raw IP datagrams without packet checksums for performance reasons, and predated the modern virtual filesystem (VFS) switch. 

---

## The Origins of Diskless Booting
Sun’s early workstations could boot without a local disk primarily to keep hardware costs down. However, the Network File System (NFS) did not appear until [SunOS 2.0](https://en.wikipedia.org/wiki/SunOS)—a release that also forced Sun to invent the [Virtual Filesystem Switch (VFS)](https://utcc.utoronto.ca/~cks/space/blog/unix/VFSImportance), a design pattern adopted by nearly every Unix variant since.

Before NFS, pre-NFS versions of SunOS achieved diskless operation using **`nd`** (the network disk). 

## How `nd` Worked
The [nd(4)](https://www.typewritten.org/Manual/Sun/SunOS/3.0/man4p/nd.html) pseudo-device driver acted as a kernel block device, routing block I/O requests over the network directly to a server kernel. 
* **Discovery:** Clients didn't need pre-configured server information; they simply broadcast their initial boot requests to find the server.
* **Server Architecture:** The same driver ran on both clients and servers, with the server-side kernel managing all requests. [nd(8)](https://www.typewritten.org/Manual/Sun/SunOS/3.0/man8c/nd.html) was used strictly for server setup.
* **Longevity:** Surprisingly, SunOS kept the `nd` infrastructure around long after NFS was introduced, finally dropping it around SunOS 4 (though it was present as early as [SunOS 1.0](https://www.typewritten.org/Manual/Sun/SunOS/1.0/man4p/nd.html) and into [SunOS 3.0](https://www.typewritten.org/Manual/Sun/SunOS/3.0/man4p/nd.html)).

## The "Cursed" Subpartitioning System
While network block devices (like iSCSI, ATA over Ethernet, or DRBD) are common today, SunOS `nd` had a unique and dangerous limitation regarding disk partitions:

> *One last type of unit is provided for use by the server. These are called local units and are named `/dev/ndl∗`. The Sun physical disk sector 0 label only provides a limited number of partitions per physical disk (eight). Since this number is small and these partitions have somewhat fixed meanings, the nd driver itself has a subpartitioning capability built-in.*

Administrators had to take a massive server partition and manually map out the starting and ending sectors for every diskless client's "disk." 

As the `nd(8)` man page dryly noted in its **BUGS** section: 
> *'no sanity checking of disk partitions is done'.*

### Living Dangerously with the "C` Partition
If an administrator ran out of the standard 8 partitions (often consumed by regular filesystems and swap space), they had to resort to using the special `'c'` partition (cf [dkinfo(8)](https://www.typewritten.org/Manual/Sun/SunOS/3.0/man8/dkinfo.html)), which covered the entire physical disk. 

Because `nd` performed no overlap or sanity checks, making a mistake meant your network disks could easily overwrite critical filesystem data. On the bright side, this manual layout allowed administrators to expose a server's `/usr` partition as a read-only "public" `nd` device, letting all diskless clients share it without needing individual copies.

## Raw IP and No Checksums
Unlike modern protocols, `nd` bypassed UDP and TCP entirely, using its own custom IP datagram protocol. According to the documentation:

> *"IP datagrams were chosen instead of UDP datagrams because only the IP header is checksummed, not the entire packet as in UDP..."*

This was done partly to simplify internal kernel interfaces, but also for performance. Running on early 1980s CPUs and Ethernet networks, skipping the checksum calculation for 1024-byte packets made a noticeable speed difference for low-powered Sun workstations. However, it meant data relied entirely on the physical reliability of early Ethernet, with zero error-checking on the wire.

Ultimately, nobody shed a tear when `nd` was phased out in favor of NFS, which utilized standard server filesystems and posed a significantly lower risk of catastrophically exploding your infrastructure.