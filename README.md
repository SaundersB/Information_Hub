# Information_Hub
A raspberry pi flask localhost server that displays time and weather information.

# Installation Instructions
1. Install Raspbian onto a Raspberry Pi >=2.
2. Purchase and install a 5" LCD display onto the Raspberry Pi.
3. Install Chromium-Browser.
4. Install Flask with Python 2.7.
5. Edit the startup configuration to boot up in kiosk mode with the Chromium Browser.
6. Set the startup configuration to land on the localhost page with the specified Flask server port.
7. Configure either a wired Ethernet connection or connect to the local wifi.
8. Notice the time, location, and weather is provided with a pleasant UI.



Note: Make sure to use `sudo shutdown -h now` to prevent file system corruption. This leads to a kernel panic.


## Install Chromium
wget https://dl.dropboxusercontent.com/u/87113035/chromium-browser-l10n_45.0.2454.85-0ubuntu0.15.04.1.1181_all.deb
wget https://dl.dropboxusercontent.com/u/87113035/chromium-browser_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
wget https://dl.dropboxusercontent.com/u/87113035/chromium-codecs-ffmpeg-extra_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
sudo dpkg -i chromium-codecs-ffmpeg-extra_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
sudo dpkg -i chromium-browser-l10n_45.0.2454.85-0ubuntu0.15.04.1.1181_all.deb chromium-browser_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb


## Install Flask
sudo apt-get install python-pip
sudo pip install flask

