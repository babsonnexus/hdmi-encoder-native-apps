---
### ALPHA WORK IN PROGRESS, NOT COMPLETE, DO NOT USE YET
---


## ADBTuner - Native Apps Configurations

![image](https://github.com/babsonnexus/adbtuner_native/blob/main/files/2026-04-11_17-48-35-ezgif.com-video-to-gif-converter.gif?raw=true)

_Demonstration of  a station playing in Channels DVR using the **ADBTuner - Native Apps Configuration** method. The client shown is the **[Feral HTPC](https://github.com/nuken/Feral-HTPC)** community user created app for Windows. Note the choppiness is just a function of being a GIF and that actual performance is smooth. See video below for a complete illustration._

### Overview and History

With the advent of the internet, many over-the-air (OTA) and cable TV channels began to stream their linear stations online. Eventually, this morphed into something known as "TV Everywhere" (TVE), which allowed users to log into websites, apps, and other such mechanisms to access their legally available—and often paid for—content. Over time, this gave rise to server applications like **[Channels DVR](https://getchannels.com/tv-everywhere)** being able to integrate these streaming stations out-of-the-box using backend logging-in and capture. As such, whether a station came from an antenna, TVE, or even custom sources such as "Free Ad-supported Streaming Television" (FAST) providers like [Pluto, Plex, Tubi, Samsung TV+, etc](https://github.com/kineticman/FastChannels)..., it was treated exactly the same. This meant every station and its content could be watched live, recorded, time-shifted, and place-shifted with ease.

Then came Digital Rights Management (DRM).

For the purpose of this explainer, DRM is a protocol that limits how digital content can be distributed by putting in place certain roadblocks that make the current methods of capturing streams not viable. To be fair, there had always been a limitation on which TVE stations were available for a variety of reasons, but DRM exacerbated the already precarious situation. While the providers generally claim DRM is an anti-piracy function, in reality it is just anti-consumer, designed to limit choice and flexibility all while pushing people inside their walled gardens. These efforts have arguably been a contributing factor to a statistically significant measured rise in piracy after nearly a decade of declines.

### Solutions and Usage

Business and politics aside, what is most important to users is being able to watch their content wherever and however they desire. Due to innovation pushed by the [Channels DVR user community](https://community.getchannels.com), there are now more options than ever to restore this expected functionality. Notably, there is **[PrismCast](https://github.com/hjdhjd/prismcast)**, which uses a method known as “Chrome Capture” to transmit what is shown on a webpage, most importantly video on TVE provider (including cable/satellite companies like Cox, Xfinity, Spectrum, DirecTV, etc...) websites. This workaround is quite useful and powerful, but is also resource intensive and can sometimes be intrusive depending upon your setup. Still, in some situations it is the only way to get what you want.

However, there is another solution known as “HDMI Encoding”. The idea is this: on your network you add a physical device that has at least one HDMI port that you put an Android TV streaming dongle (i.e., ONN, Chomecast with Google TV, FireTV, etc...) into. Then, that device captures what is showing in that HDMI port and broadcasts it out on the local network. From there, it can be received by other programs like Channels DVR, which just interprets it as any other custom station. Most important, though, is the ability to interact with the streaming dongles in order to launch apps and get to the video content you want to watch.

There are several projects around this, including **[“Android HDMI for Channels” (ah4c)](https://github.com/sullrich/ah4c)**. This tool is impressive, but there is another known as **[ADBTuner](https://adbtuner.github.io)** that is far more polished and intuitive to use. Hence, what is being presented here will focus solely on ADBTuner.

### Purpose

ADBTuner works on a few assumptions. Most critically is that it expects you to provide a “deep link” to the content that you want to launch. Basically, if you go to the content on a website, you could launch that same link on an Android TV dongle, and it would open the app and go there. This works especially well with Over-the-Top (OTT) Multichannel Video Programming Distributors (MVPDs) like YouTubeTV, Hulu with Live TV, Fubo TV, etc.... As a matter of fact, there are releases available that will give you all the stations using deep links to the MVPD providers, thus negating any need for this solution. If that is your situation, you should stop here and pursue those (although there is some general setup and advice that would still apply, should you continue).

On the other hand, without one of those MVPD providers or a situation where their apps are unavailable or unusable in this method, another approach is necessary: using native apps like ESPN, NFL, NBC, and plenty more. Nevertheless, despite their general availability, deep linking has proven to be completely unreliable or unavailable for many companies’ native apps. In order to get around this, ADBTuner can be modified with custom “Configurations” that allow automated methods of navigating around an app with human-like button pressing. More so, this project was created so that with a few basic steps, you could get the following stations (as of 2026-04-11) without having to do any additional programming:

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

All of this results in 94 stations over 10 providers and 15 apps. While this is what is available through this repository, that would not stop you from being able to get additional stations through existing and other apps. Details are discussed below, but of note:

* NBC/Comcast has additional stations available depending upon your physical location and station provider, but the number and which ones is completely variable. As such, configurations have not been included for those, but existing configurations can be easily replicated and added on to in order to have them.

* When NBC/Comcast spun off Versant for stations like MS NOW, CNBC, USA, SyFy, etc..., they also moved into their own apps. Unfortunately, those apps appear to suffer from poor engineering and either cannot log in, cannot remember TVE credentials, crash on a regular basis, or some combination thereof and other issues. Due to this, they are being excluded at this time.

* ABC/Disney retired all their native TVE apps in 2024 (aside from ESPN), as did CBS/Paramount/Skydance minus the core CBS app. As such, it is not possible to get those providers' stations using this method unless you have a cable/OTT app with them. Without something like that, it's recommended to use **PrismCast** as linked above for these stations.

* Fox has additional exclusive stations for FoxOne subscribers. Much like with NBC, the existing configurations can be replicated and added on in order to have those.

* PBS is the most variable as the number of subnets and which ones changes considerably market-to-market. The included configuration can be used as the basis for getting the remaining subnets.

* ESPN now owns NFL Network. It is highly likely in the future that NFL Network and Channel will be completely integrated into the ESPN app, necessitating an update for that entire app.

* A&E Global Media properties Lifetime and FYI can be easily added, and would use the same configurations as those for the other A&E Global Media stations.

* Other users may submit their own configurations for some of the listed above and others they may create, and those will be added to the base model. Should that occur, and you want those stations, you will need to do an update as outlined below.

### Prerequisites

In order to implement this solution, there are many things you are going to need to get, several of which can be quite expensive, and many that are going to require some technical knowledge. That said, most of it has been made as simple as possible to approach.

1. **Deploy Docker Desktop**

    * For those unfamiliar with Docker, it is fairly easy to [install Docker Desktop as a stand-alone application](https://www.docker.com/products/docker-desktop).

    * If you are installing Docker in Windows, set up Windows Subsystem for Linux (WSL) first by following [these directions](https://community.getchannels.com/t/espn-fox-sports-with-custom-channels-via-eplustv/31144/591).

    * Familiarize yourself with some [Docker basic information](https://community.getchannels.com/t/article-from-june-2021-docker-for-beginners/41078), most notably dealing with [upgrading containers](https://github.com/babsonnexus/stream-link-manager-for-channels/wiki/Upgrade-%E2%80%90-Docker) when the time comes.

2. **In Docker, install ADBTuner**

    Follow the directions in the link to ADBTuner above. Or, users who have deployed **[OliveTin for Channels]( https://community.getchannels.com/t/43380)** (including its core component **[Project One-Click](https://community.getchannels.com/t/39669)**), can use that, instead, to simplify the process.

3. **Purchase Equipment**

    You are going to need the following:

    * A modern HDMI Encoder. It is specifically recommended to get a “LinkPi” one, many of which can be found [here](https://www.youyeetoo.com/search/?Keyword=hdmi+encoder&Sort=5a&page=3). These start at around US$100 and can go over US$1000 completely as a function of power and number of HDMI ports for processing. When a port is in use, only one thing can run on it. Thus, if you are only going to watch/record one thing at a time, a single port might be all you need. But should you think you’ll watch/record four things at a time, you’ll want to invest in more expensive models or buy multiple singles over time. One of the benefits of ADBTuner is it's completely expandable at any time, so you can add or grow devices as your needs change.

    * An Android TV streaming dongle for each of those HDMI ports, which range in price from around $20 to $150. They do not have to be the same brand and, again, can be switched out as needed. Most of these have limited space, so that can also control which apps you are able to install in the next step. Storage is expandable, but again this is more costs, so it is completely up to you how far you want to go, or if you want to do more in the future.

4. **Set up Android TV Streaming Dongles**

    On your Android TV dongle(s), you need to turn on “Developer Mode” and, within “Developer Mode”, make sure USB debugging is made available. How to do this varies a bit by device and Android version, but generic directions can be found [here](https://developer.android.com/studio/debug/dev-options).

    After that, you will need to install the following native apps to use all of the stations listed before:

    * NBC
    * CBS
    * FoxOne
    * PBS
    * PBS Kids
    * ESPN
    * NFL
    * HGTV
    * CNN
    * TBS
    * TNT
    * truTV
    * A&E
    * History
    * AMC

    Depending upon your device, not all apps may be readily available. For instance, the [AMC app](https://www.apkmirror.com/apk/amc-networks/amc-fire-tv/) is missing from some devices like the Tivo Stream 4K+. In these situations, you can download the APK and sideload the app. It is highly recommended to use **[adblink](https://www.jocala.com)** for this activity.

    Once the apps are installed, you will need to go into each one and login with your TVE provider. As a pro tip, you can use the Link Pi “Push” area as your display instead of hooking up to a TV.

    ![image](https://github.com/user-attachments/assets/1a793aa9-270e-4d6c-bc4d-065c8ecc1a6b)

    You will probably want to launch each station, too, to confirm you have access as some of the providers list everything whether you can play them or not. Additionally, you may want to set other options to be on, such as closed captioning. After doing all this, it is recommended to force close each app.

5. **Finalize ADBTuner**

    Follow ADBTuner’s directions to set up your HDMI Encoder(s) and Android TV dongle(s). You should get all greens before proceeding.

    ![image](https://github.com/user-attachments/assets/5c55982b-1f61-414d-a676-634ba7a088b0)

    It is worth noting here that the specific "Streaming Endpoint" can be quite finiky. The version shown in this screenshot with the port included seems to work best (i.e., `http://[IP ADDRESS OF DEVICE]:8090/[LINK PI HDMI PORT NAME]`.

### Installation

With ABDTuner in place and configured, there are only two items needed: the configurations and the stations. With both of these placed in the proper locations and loaded, you will have access to everything shown in this repository.

1. **Configurations**

    “Configurations” are how ADBTuner knows how to act. They consist of single JSON files that contain instructions. Out of the box, ADBTuner has its own four default configurations that work great with the deep linking method, but that is not what is needed here. Instead, 81 configurations are made available for you. You can download each one individually, or all together in [this zip file](https://github.com/babsonnexus/adbtuner_native/raw/refs/heads/main/user_configurations.zip).

    After the file is downloaded, extract it completely and then move the resulting JSON files inside ABDTuner’s internal file structure under `app >> .config >> user_configurations`. It should look something like this:

    ![image](https://github.com/user-attachments/assets/6696da9d-ced8-4cc9-91cb-9f2872e65253)

    Afterwards verify that the configurations are available by navigating to that area in ADBTuner. It is critical that these exist before moving on to the next step.

   ![image](https://github.com/user-attachments/assets/392267b2-0fde-4099-bc6c-114f6b0ac3e4)

2. **Stations**

    The “stations” are the list of actual channels that you want to be able to launch. Each one is tied to a specific configuration, hence why that step is important to complete first. Similar to configurations, stations are also just a JSON file with all the pertinent details. You can navigate to the [stations JSON file](https://github.com/babsonnexus/adbtuner_native/blob/main/adbtuner_export_formatted.json) and click the button to download the raw file:

    ![image](https://github.com/user-attachments/assets/49a843e6-3819-4a3a-9513-a8c6768d269f)

    Once you have it, open the ADBTuner main webpage, navigate down to “Channels” and click the “Import / Export” link.

    ![image](https://github.com/user-attachments/assets/6d3a8f16-8bad-4c9e-b201-e39a063d11d4)

    This will bring up a menu where you can select the file and import what was downloaded.

    ![image](https://github.com/user-attachments/assets/4adec1e8-f91f-4b3a-8868-5585b5dfa274)

    You should now have all of the stations as laid out earlier.

   ![image](https://github.com/user-attachments/assets/f7056839-f165-4137-8b34-aea929466529)

### Post-Installation

With everything now in place, there are several required and optional steps to take.

1. **REQUIRED:** Update local stations (NBC, CBS, FOX, PBS)

    Unless you live in the same market as the default station list, you will want to update for your locale. This is as simple as editing the station, changing its name, and updating its Gracenote ID so it can get correct guide data.

    ![image](https://github.com/user-attachments/assets/cd9928c7-d382-4957-85e0-4222fe616e67)

    In order to get the Gracenote ID, follow the directions [here](https://community.getchannels.com/t/gracenote-guide/45587/6).

    You should also change the secondary station on your PBS lineup to match what you have, as well as add other stations, if available. See directions below.

3. **OPTIONAL:** Modify the station numbers

    The default station numbers are organized by providers, not purpose or any other logic. If you would like to change them, you are more than free to do so. Just know that within ADBTuner, that modifies the display order. There are other tools that can change the station numbers for you, too, as highlighted below.

4. **OPTIONAL:** Delete stations you don’t want

    You do not have to keep the stations you do not want, but there is no harm in maintaining them in ADBTuner and then hiding them in downstream station management tools. Given that, it is recommended to preserve all of them in ADBTuner.

5. **REQUIRED:** Test every station

    Clicking the `Preview` button with each station will allow you to watch the configurations work in action, and thus confirm everything is happening as expected. If everything is successful here, then it will also be so in all downstream apps like Channels DVR. Note that if you are using FireTV for your dongle, some apps may be a different version. In this case, you will need to edit the station and select the correct app name.

    ![image](https://github.com/user-attachments/assets/1fcc0cff-3b38-40a6-8f94-d149a99e45b6)

7. **OPTIONAL:** Adjust wait for app start times

    In the `URL` field with each station is a number. This value represents the number of seconds to wait from launching an app until actions are taken.

    ![image](https://github.com/user-attachments/assets/781c02b8-2f1f-4b15-8dea-429e96e31808)

    Based upon your device, network, internet speeds, and other factors, you may want to adjust this up or down. It is recommended to be conservative and make sure an app has enough time to load before any navigation steps are undertaken. You will be able to know if any changes are warranted by the results of the previous step.

8. **OPTIONAL:** Adjust step times

    Within the configurations, all of the various steps are shown, such as move up, down, left, right, hitting center, and others. Although these commands can be put in back-to-back, that is how a machine with no restraints would act. These apps expect a human with human reaction speeds. As such, various waits have been put in between steps to allow for this, as well as make sure certain screens load.

    ![image](https://github.com/user-attachments/assets/93020be6-da08-4c80-84c8-4a8f4fa04cce)

    These waits are controlled by the “sleep” commands, with the value next to it being the number of seconds to hold on. The default values are conservative, which means they may be taking longer than necessary for safety reasons. You are free to adjust these “sleep” times if you believe it will help speed up or slow down the process as necessary. Please see the warning below about this, though, before proceeding.

9. **OPTIONAL:** Turn off displaying loading and navigating

    As shown in the GIF above, by default, the loading of the app and the navigation steps to starting the stream are shown. This is recommended to stay that way because many of these stations will take a long time to load, including up to around 50 seconds. Some users and programs may interpret a spinning blankness to be an error and try to launch again, which would negate the sequence. However, if you are confident that is not an issue, you can turn this off.

    ![image](https://github.com/user-attachments/assets/c6213100-073a-4abd-a224-b9417b70b83d)

    The global settings shown here in the configuration can be changed to the following, then then they will no longer show the loading and navigation process.

    ```
    "use_fixed_delay": false,
    "fixed_delay_seconds": 0,
    ```

### Watch

With all of this done, you are now free to watch these stations in an outside tool like Channels DVR, VLC, and others. ADBTuner provides the necessary playlist link with all the stations to do that integration:

![image](https://github.com/user-attachments/assets/e704dd06-540e-498e-a73b-6a4f1c489172)

Just remember that, no matter the tool, the playlist must have a MPEG-TS stream format assigned to it.

![image](https://github.com/user-attachments/assets/113ebf54-b6b5-4174-9530-2419e1d46222)

While it's certainly possible to do this integration [directly into Channels DVR](https://getchannels.com/docs/channels-dvr-server/how-to/custom-channels), it is highly encouraged to use **[Playlist Manger](https://github.com/babsonnexus/stream-link-manager-for-channels/wiki/Extensions-%E2%80%90-Playlist-Manager-%5BPLM%5D)** (a **[Streaming Library Manger](https://github.com/babsonnexus/stream-link-manager-for-channels/wiki)** extension). This is because you can stack the same station from various different source playlists (“children”) and only end up with one relevant “parent” copy to play, based on a user-defined priority. That way, if one source goes away or fails, the next will seamlessly slide into place.

![image](https://github.com/user-attachments/assets/ed475098-cf79-4ece-a1a7-08e514ad708c)

Many of these stations are currently available through TVE, and therefore do not need this ADBTuner solution. Nonetheless, that might not be the case any day now, so it pays to have backups already in place and ready to go in such an eventuality. Further, **Playlist Manager** has other useful features, such as renumbernig stations, replacing logos, and much more!

### Adding New Stations and Configurations

In order to add a new station, we need to understand what steps are required to get to the live content and start playing. Tracking each one of those button presses will yield what should be in a configuration. Among some cases, the existing configurations can be used, even if they have extra steps. For instance, **AMC** uses `Up, Right x2, Down x1, Enter` even though technically the `Up` is unnecessary. More aptly, a different app from the same provider will usually have the same navigation layout, and therefore existing configurations can be used. This would be true for things like **Lifetime** and **FYI**, which should follow the same flow functionality as the other **A&E Global Media** apps.

More often, though, a configuration is needed for differing steps or additions to existing ones. Let’s look at a PBS subnet station as an example. Out of the box, this solution provides you with one subnet navigation configuration, but we might need to go down another row in the guide. A configuration to match that need is not included in this package, therefore you will have to create one. This starts by finding the existing configuration you want to base the new one on, editing it, and copying all of its contents.

![image](https://github.com/user-attachments/assets/4f364473-982f-40d4-9f9b-52d38773f875)

![image](https://github.com/user-attachments/assets/ce4a3424-f389-454c-a690-670caee9f409)

After that, we’ll want to click the link to `Add New` with the Configurations.

![image](https://github.com/user-attachments/assets/388e512b-54fc-4b34-99eb-ce8aef46dbdb)

![image](https://github.com/user-attachments/assets/e05132ed-aad3-4bab-93c2-77d43750928c)

At the bottom of the new configuration, paste what you have copied. Then, cut the line in the default values that begins with `"uuid"` and paste it over the one in the text your previously pasted. The `uuid` is a randomly generated unique identifier, so we want to make sure we always have one that differs completely from the others. This is how ADBTuner knows that there are individual and differing configurations available.

After that, you can discard everything that came with creating the new one so that only your pasted text with the new `uuid` remains. From here, you should modify the `name` row so that it contains a value to represent the button presses that need to happen. In this case, that would be:

```
"name": "Click to Play - Left, Down, Enter, Left, Down x2, Enter",
```

Then it is just a matter of what button presses you need to happen. These are generally `KEYCODE_DPAD_xxxx` functions like `UP`, `DOWN`, `LEFT`, `RIGHT`, and `CENTER`, but there is a possibility of other presses that could be useful. A complete list can be found [here](https://developer.android.com/reference/android/view/KeyEvent.html). With this example, we are just going to add another down, so we’ll want to copy the existing one and place it below:

```
"input keyevent KEYCODE_DPAD_DOWN",
"sleep 2",
```

Note again the `sleep`, which is the pause between button presses. Some apps may require more or less time depending upon how responsive they are. This time, we are being more careful than usual due to what is necessary.

_**WARNING:** The total time, including app startup, must be less than 60 seconds. If it takes more time, ADBTuner assumes the process failed and releases the tuner. Make sure your total process time stays well below this threshold to be safe, leaving plenty of contingency in case there are any hiccups._

In the end, though, we’ll end up with a configuration that looks like this:

```
{
    "name": "Click to Play - Left, Down, Enter, Left, Down x2, Enter",
    "author": "babsonnexus",
    "version": "1.0",
    "description": "Force stops an app, opens that app, and then moves as named to get an item to play. Use the 'URL' field for the delay timing the app launching until the clicks should happen.",
    "uuid": "f5e54663-ada6-41e6-93fe-691ee464bf5a",
    "global_options": {
        "wait_for_video_playback_detection": false,
        "use_fixed_delay": true,
        "fixed_delay_seconds": 1,
        "check_for_and_clear_whos_watching_prompts": false,
        "wait_after_post_playback_start_commands_seconds": 0
    },
    "pre_tune_commands": [
        "input keyevent KEYCODE_MEDIA_STOP",
        "am force-stop '||TARGET_PACKAGE_NAME||'"
    ],
    "tune_commands": [
        "monkey -p '||TARGET_PACKAGE_NAME||' -c android.intent.category.LAUNCHER -c android.intent.category.LEANBACK_LAUNCHER 1",
        "sleep ||TARGET_URL_OR_IDENTIFIER||",
        "input keyevent KEYCODE_DPAD_LEFT",
        "sleep 2",
        "input keyevent KEYCODE_DPAD_DOWN",
        "sleep 2",
        "input keyevent KEYCODE_DPAD_CENTER",
        "sleep 5",
        "input keyevent KEYCODE_DPAD_LEFT",
        "sleep 2",
        "input keyevent KEYCODE_DPAD_DOWN",
        "sleep 2",
        "input keyevent KEYCODE_DPAD_DOWN",
        "sleep 2",
        "input keyevent KEYCODE_DPAD_CENTER"
    ],
    "post_playback_start_commands": [],
    "post_tune_commands": [
        "input keyevent KEYCODE_MEDIA_STOP",
        "input keyevent KEYCODE_MEDIA_PAUSE",
        "input keyevent KEYCODE_HOME",
        "am force-stop '||TARGET_PACKAGE_NAME||'"
    ]
}
```

Save the configuration, and then it will be available to select with the new station you make.

![image](https://github.com/user-attachments/assets/136c3eea-0f05-45e5-96f7-c54a1251b1b3)

Please note that these configurations are currently not in alphabetical order, but seem to be in order by `uuid`. This can make it a bit tricky for finding the one you want. Otherwise, you can go about filling in the fields for the stations you are creating. Of key importance, when creating the station, be sure to put some textual value in the `URL` field. It doesn’t matter much, just something like `http://thing.com` will do.

![image](https://github.com/user-attachments/assets/eb2b95e7-7a1c-4c13-8e20-9074c89d467d)

Then, once you add the station, edit it again to change the `URL` to a number, that value being the seconds to wait after launching the app to start the movement sequence.

![image](https://github.com/user-attachments/assets/fe5524fc-8ce7-4cbf-93a7-65ed16af6167)

After that, all you need to do is click `Preview` and confirm it is working as expected, making any adjustments to the configuration as necessary. Otherwise, it will be available in whatever tool you use the next time you update the m3u playlist.

### Further Reading

The video below covers much of the material discussed here, but can provide a visual component to follow along with, as well:

_[VIDEO COMING SOON]_
