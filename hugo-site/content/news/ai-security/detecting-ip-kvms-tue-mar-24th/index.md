---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T05:34:56.406854+00:00'
exported_at: '2026-04-02T05:34:59.550142+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32824
structured_data:
  about: []
  author: ''
  description: 'Detecting IP KVMs, Author: Johannes Ullrich'
  headline: Detecting IP KVMs, (Tue, Mar 24th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32824
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Detecting IP KVMs, (Tue, Mar 24th)
updated_at: '2026-04-02T05:34:56.406854+00:00'
url_hash: 5829eb464e67608eb0df98b00586c7907264060c
---

I have written about how to
[use IP KVMs securely](https://isc.sans.edu/diary/32598)
, and recently, researchers at Eclypsium published yet another report on
[IP KVM vulnerabilities.](https://eclypsium.com/blog/your-kvm-is-the-weak-link-how-30-dollar-devices-can-own-your-entire-network/)
But there is another issue I haven't mentioned yet with IP KVMs: rogue IP KVMs. IP KVMs are often used by criminals. For example, North Koreans used KVMs to connect remotely to laptops sent to them by their employers. The laptops were located in the US, and the North Korean workers used IP KVMs to remotely connect to them. IP KVMs could also be used to access office PCs, either to enable undetected "work from home" or by threat actors who use them to gain remote access after installing the device on site.

IP KVMs usually connect to the system in two ways:

* USB for keyboard/mouse
* HDMI for the monitor connection (some older variants may also use VGA)

For my testing, I used two different IP KVMs. A "PiKVM" and a "NanoKVM" (Sipeed). Both were connected to Linux systems, but the techniques should work on other operating systems as well.

### USB

For the Sipeed NanoKVM, "lsusb" give away the device:

> $ lsusb
>
> Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
>
> Bus 001 Device 002: ID 0bda:c821 Realtek Semiconductor Corp. Bluetooth Radio
>
> Bus 001 Device 004: ID 051d:0002 American Power Conversion Uninterruptible Power Supply
>
>
> **Bus 001 Device 005: ID 3346:1009 sipeed NanoKVM**
>
> Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

PiKVM is a little bit less obvious, but this USB entry appears to be associated with PiVKM

> `Bus 001 Device 004: ID 1d6b:0104 Linux Foundation Multifunction Composite Gadget
>
> Bus 001 Device 017: ID 1b3f:2008 Generalplus Technology Inc. USB Audio Device`

This needs a bit more testing for the PiKVM.

### HDMI

HDMI devices send "EDID" (Extended Display Identification Data) to the system the display is connected to. The main purpose of EDID is to communicate available video modes and resolutions. But it also includes manufacturer information.

For the NanoKVM:

> `sudo get-edid | parse-edid
>
> ...
>
> Section "Monitor"
>
> Identifier "Connector"
>
> ModelName "Connector"
>
> VendorName "VCS"
>
> ...`

Not very obvious, but the "VCS" vendor name could be a reasonable indicator (check for false positives)

For PiKVM, the "Identified" and "ModelName"  are more telling:

> `Section "Monitor"
>
> Identifier "PiKVM V3"
>
> ModelName "PiKVM V3"
>
> VendorName "LNX"`

### Evasion

Of course, a more sophisticated attacker can modify these strings. PiKVM offers a configuration file to do so, in part to allow for better compatibility. I do not know whether the NanoKVM provides a similar, simple way to evade detection (but it is likely not terribly hard). So "sophisticated attacker" may translate to "able and willing to read the manual".

Many endpoint protection solutions monitor USB devices and may alert on odd devices being connected. But I am not aware of any that check monitor EDID strings. This may be another neat feature for any solutions. In office environments, most organizations provide a limited set of monitor types. For home office use, things may be more complex as users often connect their own monitors.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|