## ADBTuner - Native Apps Configurations

### Overview and History

With the advent of the internet, many over-the-air (OTA) and cable TV channels began to stream their linear stations online. Eventually, this morphed into something known as "TV Everywhere" (TVE), which allowed users to log into websites, apps, and other such mechanisms to access their legally available—and often paid for—content. Over time, this gave rise to server applications like **[Channels DVR](https://getchannels.com/tv-everywhere)** being able to integrate these streaming stations out-of-the-box using backend logging-in and capture. As such, whether a station came from an antenna, TVE, or even custom sources such as "Free Ad-supported Streaming Television" (FAST) providers like [Pluto, Plex, Tubi, Samsung TV+, etc](https://github.com/kineticman/FastChannels)..., it was treated exactly the same. This meant every station and its content could be watched live, recorded, time-shifted, and place-shifted with ease.

Then came Digital Rights Management (DRM).

For the purpose of this explainer, DRM is a protocol that limits how digital content can be distributed by putting in place certain roadblocks that make the current methods of capturing streams not viable. While the providers generally claim DRM is an anti-piracy function, in reality it is just anti-consumer, designed to limit choice and flexibility all while pushing people inside their walled gardens. These efforts have arguably been a contributing factor to a statistically significant measured rise in piracy after nearly a decade of declines.

### Solutions and Usage

Business and politics aside, what is most important to users is being able to watch their content wherever and however they desire. Due to innovation pushed by the [Channels DVR user community](https://community.getchannels.com), there are now more options than ever to restore this expected functionality. Notably, there is **[PrismCast](https://github.com/hjdhjd/prismcast)**, which uses a method known as “Chrome Capture” to transmit what is shown on a webpage, most importantly video on TVE provider (including cable/satellite companies like Cox, Xfinity, Spectrum, DirecTV, etc...) websites. This workaround is quite useful and powerful, but is also resource intensive and can sometimes be intrusive depending upon your setup. Still, in some situations it is the only way to get what you want.

However, there is another solution known as “HDMI Encoding”. The idea is this: on your network you add a physical device that has at least one HDMI port that you put an Android TV streaming dongle (i.e., ONN, Chomecast with Google TV, FireTV, etc...) into. Then, that device captures what is showing in that HDMI port and broadcasts it out on the local network. From there, it can be received by other programs like Channels DVR, which just interprets it as any other custom station. Most important, though, is the ability to interact with the streaming dongles in order to launch apps and get to the video content you want to watch.

There are several projects around this, include **[“Android HDMI for Channels” (ah4c)](https://github.com/sullrich/ah4c)**. This tool is impressive, but there is another known as **[ADBTuner](https://adbtuner.github.io)** that is far more polished and intuitive to use. Hence, what is being presented here will focus solely on ADBTuner.

### Purpose

ADBTuner works on a few assumptions. Most critically is that it expects you to provide a “deep link” to the content that you want to launch. Basically, if you go to the content on a website, you could launch that same link on an Android TV dongle, and it would open the app and go there. This works especially well with Over-the-Top (OTT) Multichannel Video Programming Distributors (MVPDs) like YouTubeTV, Hulu with Live TV, Fubo TV, etc.... Nevertheless, it has proven to be completely unreliable or unavailable for many companies’ native apps like ESPN, NFL, NBC, and plenty more. In order to get around this, ADBTuner can be modified with custom “Configurations” that allow automated methods of navigating around an app with human-like button pressing. More so, this project was created so that with a few basic steps, you could get the following stations (as of 2026-04-11) without having to do any additional programming:

* **NBC/Comcast**
  * Local NBC
  * NBC News NOW
  * NBC Sports
  * Bravo (East and West)
  * Telemundo
  * Telemundo al Dia
  * Telemundo Deportes AHORA
  * Telemundo Noticias AHORA
  * Universo (East and West)

* **CBS/Paramount/Skydance**
  * Local CBS
  * CBS News
  * CBS Sports
  * 48 Hours
  * Judge Judy
  * Hot Bench
  * Golazo! Network
  * Inside Edition
  * 60 Minutes
  * Entertainment Tonight (ET)
  * UEFA Champions League
  * Car Chase

* **Fox**
  * Local Fox
  * Fox News
  * FS1
  * FS2
  * Big 10
  * Fox Weather
  * Fox Business
  * Fox Deportes
  * TMZ
  * Fox Soul
  * The Masked Singer
  * LiveNOW from FOX

* **PBS**
  * Local PBS
  * Local PBS Subnet(s)
  * PBS Kids

* **ESPN**
  * ESPN
  * ESPN2
  * ESPNU
  * SEC Network
  * ACC Network
  * ESPNews
  * ESPN Deportes

* **NFL**
  * NFL Network
  * NFL Channel

* **Discovery Networks**
  * HGTV
  * Magnolia Network
  * Food Network
  * TLC
  * Discovery
  * Travel Channel
  * Investigation Discovery
  * Cooking Channel
  * Animal Planet
  * OWN
  * Science Channel
  * Discovery Life
  * Destination America
  * American Heroes
  * Discovery Turbo

* **Time Warner/Turner**
  * CNN
  * CNN International
  * CNN Headline News (HLN)
  * CNN Originals
  * TBS (East and West)
  * TNT (East and West)
  * truTV (East and West)

* **A&E Global Media**
  * A&E
  * The First 48
  * Live PD Presents
  * Crime 360
  * Storage Wars
  * Chaos on Cam
  * Duck Dynasty
  * Crime Cults Killers
  * Cold Case Files
  * Home.Made.Nation
  * Tiny House Nation
  * History
  * UnXplained Zone
  * Deal Zone
  * Ax Men
  * Classic Car Auctions
  * Ice Road Truckers
  * Military Heroes
  * Modern Marvels
  * Torque
  * Xtreme Outdoor

* **AMC Global Media**
  * AMC

All of this results in 88 stations over 10 providers and 15 apps. While this is what is available through this repository, that would not stop you from being able to get additional stations through existing and other apps. Details are discussed below, but of note:

* NBC/Comcast has additional stations available depending upon your physical location and station provider, but the number and which ones is completely variable. As such, configurations have not been included for those, but existing configurations can be easily replicated and added on to in order to have those.

* When NBC/Comcast spun off Versant for stations like MS NOW, CNBC, USA, SyFy, etc..., they also moved into their own apps. Unfortunately, those apps appear to suffer from poor engineering and either cannot log in, cannot remember TVE credentials, crash on a regular basis, or some combination thereof and other issues. Due to this, they are being excluded at this time.

* Fox has additional exclusive stations for FoxOne subscribers. Much like with NBC, the existing configurations can be replicated and added on in order to have those.

* PBS is the most variable as the number of subnets and which ones changes considerably market-to-market. The included configuration can be used as the basis for getting the remaining subnets.

* ESPN now owns NFL Network. It is highly likely in the future that NFL Network and Channel will be completely integrated into the ESPN app, necessitating an update for that entire app.

* A&E Global Media properties Lifetime and FYI can be easily added, and would use the same configurations as those for the other A&E Global Media stations.
