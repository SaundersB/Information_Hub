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
