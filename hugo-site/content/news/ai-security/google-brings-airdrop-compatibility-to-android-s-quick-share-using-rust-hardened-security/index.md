---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-22T00:00:07.520123+00:00'
exported_at: '2025-11-22T00:00:10.286141+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/google-adds-airdrop-compatibility-to.html
structured_data:
  about: []
  author: ''
  description: Google expands Quick Share with AirDrop support, boosts Android security,
    and blocks 115M fraud attempts in India.
  headline: Google Brings AirDrop Compatibility to Android’s Quick Share Using Rust-Hardened
    Security
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/google-adds-airdrop-compatibility-to.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Brings AirDrop Compatibility to Android’s Quick Share Using Rust-Hardened
  Security
updated_at: '2025-11-22T00:00:07.520123+00:00'
url_hash: 3e1e7367774617651cd44b1fd08b90453665b4fb
---

**

Nov 21, 2025
**

Ravie Lakshmanan

Data Protection / Technology

In a surprise move, Google on Thursday
[announced](https://blog.google/products/android/quick-share-airdrop/)
that it has updated Quick Share, its peer-to-peer file transfer service, to work with Apple's equipment AirDrop, allowing users to more easily share files and photos between Android and iPhone devices.

The cross-platform sharing feature is currently limited to the Pixel 10 lineup and works with iPhone, iPad, and macOS devices, with plans to expand to additional Android devices in the future.

In order to transfer a file from a Pixel 10 phone over AirDrop, the only caveat is that the owner of the Apple device is required to make sure their iPhone (or iPad or Mac) is discoverable to anyone – which can be enabled for 10 minutes.

Likewise, to receive content from an Apple device, Android device users will need to adjust their Quick Share visibility settings to Everyone for 10 minutes or be in Receive mode on the Quick Share page, according to a
[support document](https://support.google.com/android/answer/9286773#zippy=%2Csend-content-to-an-iphone-ipad-or-macos-device%2Creceive-content-through-quick-share)
published by Google.

"We built Quick Share's interoperability support for AirDrop with the same rigorous security standards that we apply to all Google products," Dave Kleidermacher, vice president of Platforms Security and Privacy at Google,
[said](https://security.googleblog.com/2025/11/android-quick-share-support-for-airdrop-security.html)
.

At the heart of the future is a multi-layered security approach that's powered by the
[memory-safe Rust](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html)
programming language to create a secure sharing channel that Google said eliminates entire classes of memory safety vulnerabilities, making its implementation resilient against attacks that attempt to exploit memory errors.

The tech giant also noted that the feature does not rely on any workaround and that the data is not routed through a server, adding it's open to working with Apple to enable "Contacts Only" mode in the future.

"Google's implementation of its version of Quick Share does not introduce vulnerabilities into the broader protocol's ecosystem," NetSPI, which carried out an independent assessment in August 2025, said.

"While it shares specific characteristics with implementations made by other manufacturers, this implementation is reasonably more secure. In fact, the process of file exchange is notably stronger, as it doesn't leak any information, which is a common weakness in other manufacturers' implementations."

That said, its analysis uncovered a low-severity information disclosure vulnerability (CVSS score: 2.1) that could permit an attacker with physical access to the device to access information, such as image thumbnails and SHA256 hashes of phone numbers and email addresses. It has since been addressed by Google.

The development comes as Google said it blocked in India more than 115 million attempts to install sideloaded apps that request access to sensitive permissions for financial fraud. The company also said it's piloting a new feature in the country in collaboration with financial services like Google Pay, Navi, and Paytm to combat scams that trick users into opening the apps when sharing their screens.

"Devices running Android 11+ now show a prominent alert if a user opens one of these apps while screen sharing on a call with an unknown contact," Evan Kotsovinos, vice president of privacy, safety, and security at Google,
[said](https://blog.google/intl/en-in/company-news/protecting-vulnerable-audiences-is-at-the-heart-of-ai-safety-efforts/)
. "This feature provides a one-tap option to end the call and stop screen sharing, protecting users from potential fraud.

Lastly, Google said it's also developing Enhanced Phone Number Verification (ePNV), which it described as a new Android-based security protocol that replaces SMS OTP flows with SIM-based verification to improve sign-in security.