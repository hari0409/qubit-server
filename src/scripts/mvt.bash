#!/bin/bash

# sudo apt install python3 python3-pip libusb-1.0-0 sqlite3 adb -y
export PATH=$PATH:~/.local/bin
pip3 install mvt
mvt-android check-adb
MVT_VT_API_KEY=bbd8601173d83df946b1de0a6f6236e0adf4fbc3710815acee342522f3c64d0a mvt-android download-apks --output apps --virustotal >> /home/$USER/Downloads/mvt_analysis.txt
rm -rf ./apps