# nmyv (Native Messaging Youtube Viewer)
This is a simple browser extension that makes use of the Native Messaging API to allow users to quickly open a YouTube video in a pop-out `mpv` window.
Most of the heavy lifting of this task is handled by the excellent `youtube-viewer` [app by trizen](https://github.com/trizen/youtube-viewer) and `nativemessaging` [Python library by Rayquaza01](https://github.com/Rayquaza01/nativemessaging).
This project consists of a relatively pedestrian Chromium extension that adds a button and a context menu item for opening YouTube videos.
On either event, the extension passes the video ID to a small Python host which verifies everything and then opens the video, with an instance of `youtube-viewer` running in a `tmux` session.

## Installation

* Make sure that you have a copy of `youtube-viewer`, `python`, `tmux` and `mpv` installed and on your path.
* Install the `nativemessaging` API however you choose; the easiest method is `pip3 install nativemessaging`.
* Navigate to wherever you would like to install the host; this folder must not be altered after installation.
* Clone the project with
```
git clone https://github.com/tomchaplin/nmyv.git
```
* Navigate into the project directory and run the install script `install.sh`.
* This will alter the host manifest file to point at the current location of the host and install this manifest in
```
$HOME/.config/chromium/NativeMessagingHosts/com.tom.nmyv.json
```
* Open Chromium to `chrome://extensions` then drag and drop the extension package `nmyv.crx` from a graphical file manager.
* Enjoy.

### Window Manager Configuration

The host is setup to open `mpv` with the additional argument of `--x11-class="nmyv"`.
Users of window managers like `i3` can take advantage by automatically floating and resizing the window.
On `i3` this can be achieved with
```
for_window [instance="nmyv"] floating enable, resize set 640 210, move absolute position center
```

## Usage

When currently watching a YouTube video, click the `nmyv` logo next to the address bar or in the options menu to pause the video and pop-out a copy of the video.
The video should start from where you left off.
If you are browsing YouTube for videos to watch, right click on a link to a video and select the option "Open with nmyv" to pop-out a copy of the video.

## Limitations

* The project currently only works with Chromium, although a quick tweak of the install script would allow Google Chrome usage.
Firefox support should be possible but might be more involved.
* Currently this is only written for Linux, although should in principle be possible for Windows and MacOS.
* More configuration options available through `youtube-viewer` could be exposed through a simple config file or through an interface in Chromium.
* It would be nice if pressing the button again would resume the video in browser, picking up where you left off.
