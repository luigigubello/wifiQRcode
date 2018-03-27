# wifiQRcode
Print a QR code in the terminal with the credentials of the wireless network

## Info
Test with Python 2.7.9 on Debian Jessie. The module python-wifi doesn't work with Python 3.x.<br/>
This code prints a QR code in the terminal with the credentials of the wireless network. It is useful if you want to connect a phone to wi-fi without typing the password.<br/>
<i>You must have network-manager installed.</i>

## To start
pip install python-wifi<br/>
pip install qrcode<br/>
python wifiqr.py
