---
### ALPHA WORK IN PROGRESS, NOT COMPLETE, DO NOT USE YET
---


## HDMI Encoder Native Apps

![image](https://github.com/babsonnexus/hdmi_encoder_native_apps/blob/main/.gitfiles/2026-04-11_17-48-35-ezgif.com-video-to-gif-converter.gif?raw=true)

_Demonstration of  a station playing in Channels DVR using the **HDMI Encoder Native Apps - ADBTuner** method. The client shown is the **[Feral HTPC](https://github.com/nuken/Feral-HTPC)** community user created app for Windows. Be aware that the choppiness is just a function of being a GIF and that actual performance is smooth. See video below for a complete illustration._

_**NOTE:** Screenshots and videos may be slightly out-of-date as functionality and formatting are updated, but the activities will always be accurate._

### Overview and History

With the advent of the internet, many over-the-air (OTA) and cable TV channels began to stream their linear stations online. Eventually, this morphed into something known as "TV Everywhere" (TVE), which allowed users to log into websites, apps, and other such mechanisms to access their legally available—and often paid for—content. Over time, this gave rise to server applications like **[Channels DVR](https://getchannels.com/tv-everywhere)** being able to integrate these streaming stations out-of-the-box using backend logging-in and capture. As such, whether a station came from an antenna, TVE, or even custom sources such as "Free Ad-supported Streaming Television" (FAST) providers like [Pluto, Plex, Tubi, Samsung TV+, etcetera](https://github.com/kineticman/FastChannels), it was treated exactly the same. This meant every station and its content could be watched live, recorded, time-shifted, and place-shifted with ease.

Then came Digital Rights Management (DRM).

For the purpose of this explainer, DRM is a protocol that limits how digital content can be distributed by putting in place certain roadblocks that make the current methods of capturing streams not viable. To be fair, there had always been a limitation on which TVE stations were available for a variety of reasons, but DRM exacerbated the already precarious situation. While the providers generally claim DRM is an anti-piracy function, many people, including this author, find it to be just anti-consumer, designed to limit choice and flexibility all while pushing people inside their walled gardens. These efforts have arguably been a contributing factor to a statistically significant measured rise in piracy after nearly a decade of declines.

### Solutions and Usage

Business and political opinions aside, what is most important to users is being able to watch their content wherever and however they desire. Due to innovations primarily advanced by the [Channels DVR user community](https://community.getchannels.com), there are now more options than ever to restore this expected functionality. Notably, there is **[PrismCast](https://github.com/hjdhjd/prismcast)**, which uses a method known as “Chrome Capture” to transmit what is shown on a webpage, most importantly video on TVE provider (including cable/satellite companies like Cox, Xfinity, Spectrum, DirecTV, etcetera) websites. This workaround is quite useful and powerful, but is also resource intensive and can sometimes be intrusive depending upon your setup. Still, in some situations it is the only way to get what you want.

However, there is another solution known as “HDMI Encoding”. The idea is this: on your network you add a physical device that has at least one HDMI port that you put a streaming dongle (i.e., ONN, Chromecast with Google TV, FireTV, TiVO Stream, Roku, etcetera) into. Then, that device captures what is showing in that HDMI port and broadcasts it out on the local network. From there, it can be received by other programs like Channels DVR, which just interprets it as any other custom station. Most importantly, though, is the ability to interact with the streaming dongles in order to launch apps and get to the video content you want to watch.

There are several projects around this, including **[“Android HDMI for Channels” (ah4c)](https://github.com/sullrich/ah4c)**. This tool is impressive, but there is another that focusses on Android TV capture known as **[ADBTuner](https://adbtuner.github.io)** that can subjectively be seen as far more polished and intuitive to use. And although ABDTuner is the prefererd method for Android-based capture, for Roku sticks the main option is **[Roku Bridge](https://tuner.ct.ws/)**, which has similar functionality and performance. Together, these two are the focus of this instrument.

### Purpose

**ADBTuner** and **Roku Bridge** work on a few assumptions. Most critically is that they generally expect you to provide a “deep link” to the content that you want to launch. For instance, if you go to the material on a website, you could launch that same link on a streaming dongle, and it would open the app and go to that same location. Sometimes, though, the apps have their own deep linking methodology, such as replacing `http` with the app name or something similar. Either way, this approach works especially well on Android-based systems with Over-the-Top (OTT) Multichannel Video Programming Distributors (MVPDs) like YouTubeTV, Hulu with Live TV, Fubo TV, etcetera. As a matter of fact, there are releases available that will give you all the stations using deep links to the MVPD providers, thus negating any need for this solution. If that is your situation, you should stop here and pursue those (although there is some general setup and advice that would still apply, should you continue).

On the other hand, without one of those MVPD providers or a situation where their apps are unavailable or unusable in this method, another approach is necessary: using native apps like ESPN, NFL, NBC, and plenty more. Nevertheless, despite their general availability, deep linking has proven to be completely unreliable or unavailable for many companies’ native apps. In order to get around this, ADBTuner and Roku Bridge can be modified with custom “Configurations” or "Plugins" that allow automated methods of navigating around an app with human-like button pressing. More so, this project was created so that with a few basic steps, you could get all or a subset of the available stations without having to do any additional programming.

### Information, Installation, and Setup

Details for everything can be found in the Wiki:

* **[Available Stations](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Stations-%E2%80%90-Available)**

* **Setup**
  * **[Prerequisites](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Setup-%E2%80%90-Prerequisites)**
  * **[Installation](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Setup-%E2%80%90-Installation)**
  * **[Post-Installation](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Setup-%E2%80%90-Post%E2%80%90Installation)**
  * **[Adding New Stations](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Stations-%E2%80%90-Adding-New)**

* **[Watch](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/General-%E2%80%90-Watch)**

### Further Reading and FAQ / Troubleshooting

The video below covers much of the material discussed here, but can provide a visual component to follow along with, as well:

_[VIDEO COMING SOON]_

Otherwise, perhaps [one of these](https://github.com/babsonnexus/hdmi_encoder_native_apps/wiki/FAQ-and-Troubleshooting) can answer your query...
