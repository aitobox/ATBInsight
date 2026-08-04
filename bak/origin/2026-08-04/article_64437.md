# The Ubuntu 26.04 Server Installer and Reusing Existing Data Filesystems

## Summary
When upgrading Ubuntu servers (such as from 22.04 or 24.04 LTS to 26.04 LTS) using a network reinstall system, preserving separate local data filesystems is a major concern. While the Ubuntu 26.04 server installer offers options to recognize and mount existing RAID arrays without formatting, practical testing suggests the installer may still reformat designated mount points. To guarantee data safety—especially for irreplaceable historical data—physical disconnection or migrating to new hardware remains the most reliable strategy.

---

## The Upgrade Scenario
Suppose you manage Ubuntu servers featuring local data filesystems (containing critical data) residing on separate disks distinct from your system disks. As you plan an update from Ubuntu 22.04 or 24.04 LTS to 26.04 LTS—utilizing a [kexec-based network reinstall system](https://utcc.utoronto.ca/~cks/space/blog/linux/UbuntuServerInstallerInitramfs)—your primary objective is executing an in-place reinstall without destroying your existing data filesystems.

## Installer Capabilities vs. Reality
The Ubuntu 26.04 server installer introduces promising features for this exact scenario:
* It recognizes existing software RAID arrays, allowing you to avoid touching them.
* It theoretically allows you to instruct the installer to mount an extra RAID array as an `ext4` filesystem without formatting it.

However, in practice, **the installer appears to reformat anything designated for a mount point**, regardless of instructions not to do so. Whether this behavior stems from a bug or misconfiguration, relying on the installer to leave intact data untouched carries significant risk. 

*(Note: The installer is capable of leaving disks entirely alone—otherwise, it would overwrite the USB memory stick it boots from. However, standard workflows generally exclude the installer medium from manual partitioning.)*

## Recommended Best Practices for Data Safety
When dealing with critical assets—such as [years of historical metrics data](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019)—caution is paramount:

1. **Physical Removal:** If you care deeply about your data during an in-place reinstall, physically remove the data disks beforehand.
2. **Hardware Migration:** If you are already removing the data disks and possess spare hardware, a safer workflow involves installing the OS on new hardware and subsequently migrating the data disks over. 
3. **Thorough Testing:** Any in-place reinstall requires rigorous preliminary testing to confirm that disks and software RAID arrays remain unaltered. Even then, complete trust in the installer's edge-case handling is difficult to justify.

## Post-Install Considerations
Even if an automated reinstall succeeds, several manual steps remain necessary:
* **RAID Naming:** Correct the software RAID array's name by explicitly adding it to `/etc/mdadm/mdadm.conf` to prevent default naming assignments like `md127`.
* **Filesystem UUIDs:** Preserve the old system's `/etc/fstab` to reference the correct UUIDs for mounting your data filesystems.

## Practical Application
This dilemma often arises in virtualization testing environments running older releases like Ubuntu 22.04. While administrators [know how to manually migrate setup configurations](https://utcc.utoronto.ca/~cks/space/blog/linux/LibvirtMovingSetup), a streamlined network reinstall—followed by remounting `/virt` to restore VM images and replacing select configuration files—would dramatically accelerate the upgrade process and enable remote execution entirely from the office.