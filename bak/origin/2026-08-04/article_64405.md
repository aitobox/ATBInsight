# Gadget Review: HIKMICRO D02 Thermal Camera ★★★★★

## Summary
The **HIKMICRO D02** is a budget-friendly thermal imager from the company's "Eco" series, designed for home diagnostics such as spotting water leaks, insulation gaps, and overheating electrical components. Retailing around £170–£190, it punches well above its weight class by combining thermal and optical images into a single "fusion" view, supporting Linux and open-source licensing, and even functioning as a UVC webcam. Despite minor physical quirks and limited internal storage (around 2.5GB), its ease of use, utility, and clever features make it one of the best value-for-money thermal cameras on the market.

---

## Table of Contents
- [Specs and Pictures](#specs-and-pictures)
- [Videos](#videos)
- [Features](#features)
- [SuperScene AI](#superscene-ai)
- [User Interface](#user-interface)
- [Linux and Open Source](#linux-and-open-source)
- [Webcam](#webcam)
- [Price](#price)
- [Final Thoughts](#final-thoughts)

---

## Specs and Pictures

![A thermal camera with a screen and a trigger.](http://localhost/proxy/J0aLgcAqH2RTVb1Ph0rKE06VJn_QW8dDG5c7VbsmfDE=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA3L0QwMi53ZWJw)

Infrared cameras usually feature *tiny* sensors, and the D02 is no different: it packs **96x96 pixels** of thermal data upscaled to **240x240**. 

Where the D02 truly shines is its dedicated *optical* camera (480x640 resolution) positioned just below the thermal sensor. This allows the device to blend both feeds into a single "fusion" image, giving you the best of both worlds.

* **Thermal Image (240x240):**
  ![Thermal image with heat data on screen.](http://localhost/proxy/Z4MkZvPYRvS2JZ7ptKiT1K2ERSc_IUejAfnaAAB7_Yw=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L3RoZXJtYWwuanBlZw==)

* **Visual Image (480x640):**
  ![Photo of a plug by a consumer unit.](http://localhost/proxy/CP9xWod-6fYto_cfK4cMr6vlYSDS4Oti9qpsvJZcyTE=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L3Zpc3VhbC5qcGVn)

* **Fused Image:**
  ![A thermal photo with lots more visual detail.](http://localhost/proxy/H5xCy0di8xvXlEEWKjOyyyp0LVMRJr7gj6dEeBm_bPM=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L2Z1c2VkLmpwZWc=)

While the fusion technique works remarkably well for standard distances, objects extremely close to the lens can result in slight parallax alignment offsets:

![A photo of my hand. The thermal image is slightly offset from the visual image.](http://localhost/proxy/Q15NKhx5JSDug9c46Q5pn6VM7by0-0yDjbtmHFL19rw=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L2FsaWdubWVudC5qcGVn)

Storage is capped at approximately **2.5GB** with no SD card slot. However, because photos are typically under 150KB, you can store tens of thousands of images before needing to clear space.

---

## Videos

Videos average around **12MB per minute** in MP4 format (captured at 240x240 upscaled). While they lack audio, they are more than adequate for domestic troubleshooting.

<video width="240" height="240" src="https://shkspr.mobi/blog/wp-content/uploads/2026/08/pot-boiling-1.mp4" controls=""></video>

### EXIF Data
EXIF metadata is sparse—limited to timestamps and the camera serial number. Fortunately, images and videos are neatly organized in a standard `DCIM` folder for easy importing.

---

## Features

The D02 includes several handy utility settings:
* **Scheduled Capture:** Set the camera on a tripod to take periodic photos automatically.
* **Color Palettes:** Swap between various visual profiles to best highlight specific thermal differentials.
* **Emissivity & Distance Profiles:** Calibrate the sensor based on the material you are scanning and your distance from it.
* **Thermal Alarms:** Set alerts for objects exceeding high or low-temperature thresholds.
* **On-Device Playback:** Review photos and videos directly on the screen without needing a computer.

![Thermal image showing a hot USB charger.](http://localhost/proxy/JRQzXDCp3zGNrHoWSsbSfE4me43DtczD8Qn0A1sVrnI=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA3L0hNMjAyNjA3MjFfMTcxOTIzLmpwZWc=)

---

## SuperScene AI

Updating to the latest firmware introduces **SuperScene AI**, which automatically analyzes photos for common household anomalies.

![Scenes include Water Leak, Insulation, floor heating, electrical faults, solar panel.](http://localhost/proxy/xKUYyNLRaFD96sbTunEYEqQuJC0LkxOYMs-utH_Mo4o=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L1N1cGVyLVNjZW5lLndlYnA=)

Simulating a water leak under a sink, the camera successfully outlined the cool area in red and added a water droplet icon in the corner:

![A thermal image with a blue area highlighted with a red outline.](http://localhost/proxy/agK_t7nk3B6Yj1zE1PO6A3eq_u56cG6ESOCNIChG4-M=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L0hNMjAyNjA4MDNfMTQ0NzAxLmpwZWc=)

---

## User Interface

* **The Trigger:** Pull once to snap a photo; hold down to start/stop video recording. Idiot-proof.
* **The Buttons:** The layout features a combined power/select button, a back button, and up/down arrows. (Note: The up arrow changes the photo mode, while the down arrow switches the color scheme). 
* **Build:** No touchscreen, haptic feedback, or expensive speakers—keeping it rugged and simple.

---

## Linux and Open Source

The D02 mounts seamlessly on Linux systems as a standard USB storage device (`0525:a4a5` "Netchip Technology, Inc. Linux-USB File-backed Storage Gadget"). 

Unlike many hardware manufacturers that ignore open-source obligations, HIKMICRO includes a dedicated settings menu displaying software names and licenses. **A bonus star for that!**

![Open source statements shown on the camera screen.](http://localhost/proxy/NgugC0sB-m-FvBCxkimcXzhBpEO60By86j22ULp4VSc=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA4L0ltYWdlcGlwZV81My53ZWJw)

---

## Webcam

Plugging the camera in via USB-C offers a choice between **"USB Drive"** or **"USB Cast Screen"**. Selecting the latter transforms the unit into a UVC WebCam (`2bdf:017f`). 

Using tools like `qv4l2` on Linux, it can stream MJPG video once set to 240x320 resolution:

![Screenshot of a thermal image of a smiling man.](http://localhost/proxy/mZlwTxuq6m31aFT3bd_Q1l94Od2GJIT5dmQz4JsR0VY=/aHR0cHM6Ly9zaGtzcHIubW9iaS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI2LzA3L1dlYmNhbS53ZWJw)

Supported formats via `v4l2-ctl`:
```text
ioctl: VIDIOC_ENUM_FMT
    Type: Video Capture

    [0]: 'MJPG' (Motion-JPEG, compressed)
        Size: Discrete 240x320
            Interval: Discrete 0.033s (30.000 fps)
        Size: Discrete 320x240
            Interval: Discrete 0.033s (30.000 fps)
    [1]: 'YUYV' (YUYV 4:2:2)
        Size: Discrete 640x256
            Interval: Discrete 0.033s (30.000 fps)
```

---

## Price

Infrared cameras are notoriously expensive, making the D02’s **£170–£190** price tag quite reasonable. Considering it can help you locate costly insulation gaps or prevent electrical hazards, it pays for itself quickly.

---

## Final Thoughts

Having reviewed numerous thermal cameras, the HIKMICRO D02 easily stands out as a favorite. The optional fusion of thermal and optical imagery makes diagnosing home problems intuitive and straightforward. 

It is lightweight, quick to boot, accurate, and reasonably priced. Highly recommended for homeowners looking to check for leaks, drafts, and hotspots—consider splitting the cost with neighbors or borrowing it out via a local tool library.