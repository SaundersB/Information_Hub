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
```
wget https://dl.dropboxusercontent.com/u/87113035/chromium-browser-l10n_45.0.2454.85-0ubuntu0.15.04.1.1181_all.deb
wget https://dl.dropboxusercontent.com/u/87113035/chromium-browser_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
wget https://dl.dropboxusercontent.com/u/87113035/chromium-codecs-ffmpeg-extra_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
sudo dpkg -i chromium-codecs-ffmpeg-extra_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
sudo dpkg -i chromium-browser-l10n_45.0.2454.85-0ubuntu0.15.04.1.1181_all.deb chromium-browser_45.0.2454.85-0ubuntu0.15.04.1.1181_armhf.deb
```

## Install Flask
```
sudo apt-get install python-pip
sudo pip install flask
```


## Autoboot Chromium Browser
1. Edit your autostart file.
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```
2. Add these lines to the file.
```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
#@xscreensaver -no-splash
# Auto run the browser
@xset s off
@xset -dpms
@xset s noblank
@sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium/Default/Preferences
@chromium-browser --noerrdialogs --kiosk http://192.168.1.100:8080
```

## Autoboot Flask Server
1. Open your crontab configuration file with the following command:
```
crontab -e
```
4. Add the following line to your crontab configuration file:
```
@reboot python /home/pi/src/Information_Hub/app.py &
```

## Install Python Library Dependencies
```
sudo pip install IP2Location
sudo pip install geocoder
```
