# Kodi Setup Guide

## Hardware Requirements

- RAM: >= 8 GB
- Storage: >= 1 GB of free disk memory
## Installation for Ubuntu 22.04 on X86 HW

Kodi can be [installed](https://kodi.wiki/view/HOW-TO:Install_Kodi_for_Linux?https=1) on Ubuntu by adding the Kodi PPA. If you've installed Kodi already through your system (i.e. with ```apt```), remove it first with ```sudo apt purge kodi\*``` then install by:
```bash
sudo apt install software-properties-common
sudo add-apt-repository -y ppa:team-xbmc/ppa
sudo apt install kodi
```

**Now Kodi can be started!**

For reference, to uninstall Kodi:
```bash
sudo apt purge kodi\*
tar cf - "${HOME}/.kodi/" | xz -z9e - >"${HOME}/kodi-backup_$(date +%m%d%y-%H%M).tar.xz"
rm -Ri "${HOME}/.{kodi,xbmc}/"
```

## Installation for LibreELEC on a Raspberry Pi 5

LibreELEC is "Just enough OS" for Kodi to run. It is perfect if Kodi is the only purpose for a device such as a Raspberry Pi.
### Items Used

- Raspberry Pi 5
- Wireless keyboard
- Micro-SD card
- Micro-SD to USB adapter
- Micro HDMI to HDMI
- Ethernet cable (not required)
### Installation

Using the Raspberry Pi Imager, we can flash a micro-SD card with LibreELEC. First insert a the micro-SD card into the computer. In my case, I used a micro-SD to USB adapter. Then launch the Imager app. When choosing the Operating System in the Imager, select `Media Player OS` > `LibreELEC` > `LibreELEC (RPi5)`. Select the micro-SD card in the Storage menu. Then select `Write`. After the Imager tells you that it has finished, the micro-SD card can be removed and put into the Raspberry Pi.
### Setup

On the first startup, Kodi will prompt you for the language. After pressing next, the hostname can be configured. I changed my hostname to something more fun but it is not that important. The next item to configure is for networking. Go ahead and select the network to use and enter the password. Once the network is online, hit next. For `Sharing and Remote Access`, Samba is enabled by default and I enabled SSH. The default user and password is `root`:`libreelec`. After enabling SSH, Kodi will prompt you to change the root password. The next section is a thank you message as initial setup is complete!
## Modify Some Settings

From the base page of Kodi, select the settings icon. When in each menu, make sure the ```Expert``` settings are being displayed. This can be toggled in the bottom left of the screen. The following settings changes have been copied from a [guide](https://www.reddit.com/r/Addons4Kodi/comments/zzfdtb/allinclusive_kodi_guide_for_beginners_movie_and/) on Reddit.
- Player > Language > Preferred audio language = English (Important - Prevent streams from defaulting to foreign audio)
- Player > Language > Preferred subtitle language = English (Important - Prevents streams from defaulting to foreign subtitles)
- Media > General > Show parent items = Off (Prevents a back button being shown that leads to your file manager when navigating a series' season later in the guide)
- Interface > Regional = Configure regional settings to your preference
- System > Display = Ensure correct resolution is set
- System > Display > Use Fullscreen Window = On (if decent PC) or Off (if low-powered PC). Makes swapping between apps easier on Windows if on, but uses more resources.
- System > Addons > Unknown Sources = On (Required to install 3rd party addons)
## Adding the [Open Wizard Respository](https://a4k-openproject.github.io/repository.openwizard/)

1. Open Kodi and Select the gears icon
2. Select the ```File Manager```
3. Select ```Add Source```
4. Select the ```<None>``` attribute and enter ```https://a4k-openproject.github.io/repository.openwizard/```
5. Hit enter
6. Give the add-on a name like ```Open Wizard```
7. Return to the settings menu and select ```Add-ons```
8. Select ```Install from zip file```
9. Select ```Open Wizard``` then select the zip file
10. Go back and select ```Install from repository```
11. Select ```OpenWizard Repository```, ```Program add-ons```, and ```OpenWizard```
12. Open Wizard is now installed!
## Other Add-ons to Install

- [Umbrella](https://github.com/umbrellaplug/umbrellaplug.github.io): https://umbrellaplug.github.io/
- A4K Subtitles: https://a4k-openproject.github.io/a4kSubtitles/packages
- [CocoScrapers](https://github.com/CocoJoe2411/repository.cocoscrapers): https://cocojoe2411.github.io/
## Kodi Add-ons to Install

`Settings` > `Add-ons` > `Install from respository` > `Kodi Add-on repository` > Category > Add-on
- Context menus
	- Trakt - Add to watchlist button
	- Trakt - Context menu
	- Trakt - Watched button
	- Trakt - Rating button
- Program Add-ons
	- Log Viewer for Kodi
		- View logs in the browser or within Kodi
	- Trakt
	- Wikipedia
		- Usable within the information menu
## Changing the *Skin*

The default skin is Estuary which sometimes has issues with add-ons. Switching skins can fix this. It also seems like if you go back to Estuary after, then it would fix the problem.

1. Enter Settings
2. Select `Interface`
3. Select `Skin` from the left menu
4. Select `Skin` from the options menu
5. Navigate to ```Get More``` and select `Arctic: Zephyr - Reloaded (AZR)`

I will be using AZR for the remainder of this tutorial.
## Configuring Umbrella

The add-on settings can be found in `Settings` > `Add-ons` > `My add-ons` > `Video add-ons` > `Umbrella` > `Configure`.
### Enable CocoScrapers for Umbrella

After entering the configuration menu for Umbrella, make your way to the `Providers` tab on the left menu. Check the box beside `Enable External Providers` then select the `External Provider:` option. Scroll down and select `CocoScrapers`.
### Linking Real Debrid to Umbrella

Staying within the configuration menu, enter the `Accounts(Debrid)` tab. You will need a real-debrid account before linking to your Kodi installation. Select `Authorization`, then using the [provided link](https://real-debrid.com/device), go to real-debrid and enter the code to Authorize Kodi. After authorizing Umbrella, the link and code will automatically go away.
### Linking Trakt to Umbrella

In the configuration menu, enter the `Trakt` tab and select `Authorization`. A pop up with a trakt.tv [link](https://trakt.tv/activate) and a code will be provided. A trakt account will be needed for this to work. After authorizing Umbrella, the link and code will automatically go away.
### Sources Sorting and Filtering

In the Umbrella configuration menu, under the `Sorting and Filters` tab, we can optimize which source options we're given when trying to watch something . Under the `Source Filtering Options`, we can set the `Max Quality` to whatever device we are using can handle. For me that is 1080p. I also set a max size for movies of ~15 GB. Then further down, we can turn off a removed duplicates popup. Also, in the `Source Filtering (Video)` section, select `Remove Dolby Vision`.
### Continuous Play for TV Shows

Under `TV Shows` > `Continuous Episode Playback Settings`
- `Enable PlayNext popup`
- Enable `- Continue to next season (if available)`
## Trakt Configuration

In the Trakt configuration menu:
- Enable Scrobbling for Movies and for T.V. shows
- Enable `Sync collection on library update or cleaning`
- Enable `Sync movie playback progress to Kodi`
- Enable `Sync episode playback progress to Kodi`
- Disable `Rate Movie after watching`
- Disable `Rate TV show Episode after watching`
## Log Viewer for Kodi Configuration

- Enable `Invert Log`
- `Enable HTTP server`

After enabling the HTTP server, going to `<address>:8080` will bring up the logs.
## Subtitles Configuration

Not specifically A4K configuration, but in Kodi settings, set A4K as the default subtitle source.
- `Settings` > `Player` > `Subtitles` > `Default TV show service` = `arkSubtitles`
- `Settings` > `Player` > `Subtitles` > `Default movie service` = `arkSubtitles`
## Configuring the Kodi GUI

Change the menu layout with `Settings` > `Skin settings` > `Home` > `Home menu style` > `Vertical Multi-Widgets`

Now to add to the menu layout. `Settings` > `Skin settings` > `Home` > `Customize home menu`
- On `Videos`, tap to the left until hovering over the `+`
- Hit `Enter`
- A blank item labeled `<None>` with appear
- This first one will be the `Explore` page
- First we can select an action item
- Select `Choose item for menu` > `Add-on` > `Video Add-on` > `Umbrella` > `Search` > `Create menu item to here`
- Now select `Label` and change the name to `Explore`
- Finally onto widgets
- Select `Widget 1` > `Widget 1` > `Add-On` > `Video Add-On` > `Umbrella` > `Discover Movies` > `Trending (Trakt)` > `Use as Widget` > Name this `Trending Movies`

This process can be repeated for any tabs made to add action items and widgets. Additional widgets are disabled by default. Listed below is the setup I use.

**My Configuration**
- Explore
	- Action: Search Menu
	- Widgets:
		- Trending Movies
		- Trending TV Shows
		- Popular Movies
		- Popular TV Shows
		- Featured Movies
		- Highly Rated TV Shows
- Movies
	- Action: Search Movies
	- Widgets:
		- In Progress
		- Watchlist
		- Recommended
		- Based on Recently Watched
		- Similar to Recently Watched
- TV Shows
	- Action: Search TV Shows
	- Widgets:
		- In Progress (Shows)
		- Watchlist
		- Recommended
		- Based on Recently Watched
		- Similar to Recently Watched
- Watched
	- Widgets:
		- Watched Movies
		- Watched TV Shows
- Settings
	- Action: Open Settings
	- Widgets:
		- Settings
		- System Info
- Power
	- Action: Open Power Menu
## Clearing Cache with Open Wizard

This is useful in case an add-on fails to install in the future. Go to `Settings` > `Add-ons` > `My add-ons` > `Program add-ons` > `Open Wizard` > `Launch`. In Open Wizard, select the `Maintenance` tab, then select `Cleaning Tools`, and lastly `Total Clean Up`. This will clear the cache, packages, and thumbnails.
## Notes

- To edit or remove a source in the ```File Manager```, press ```c``` while hovering over the source.
- The `Reboot` option in the `Power Menu` reboots the computer.
## Keyboard Shortcuts

- `i`: Opens information page
- `c`: Opens context menu
- `Backspace`: Go back one level
- `Esc`: Escape to top the top level
## References and Resources

- [Reddit Guide](https://www.reddit.com/r/Addons4Kodi/comments/zzfdtb/allinclusive_kodi_guide_for_beginners_movie_and/)
- [LibreELEC.tv](https://libreelec.tv/)
- [Raspberry Pi Software](https://www.raspberrypi.com/software/)
## Issues

Umbrella is not scraping for content
- Received notification: `External providers are enabled but...`
- Solution: Make sure CocoScrapers is selected as the `External Provider`
## Controlling Kodi

I primarily use a wireless keyboard when setting up Kodi, but that isn't ideal for regular use. Other options include using an add-on for controller support, the mobile app for phone control, or (as I am doing now) a miniature wireless keyboard. The mini keyboard I am using now is a Rii miniature wireless keyboard.

![Rii Miniature Wireless Keyboard with Trackpad](../images/rii_mini_keyboard.jpg)