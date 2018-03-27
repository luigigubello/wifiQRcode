#!/usr/bin/python

# https://github.com/luigigubello/
# Test with Python 2.7.9 on Debian Jessie. It doesn't work with Python 3.x.
# pip install python-wifi
# pip install qrcode

import os
import sys
import qrcode
from pythonwifi.iwlibs import Wireless

if os.getuid() != 0:
	print('\n    Need to be root, sorry.\n')
	sys.exit()

wifi = Wireless('wlan0')
ssid = str(wifi.getEssid())
if ssid=='':
	print('\n    Need to be connect to Wireless Network.\n')
	sys.exit()
hidden = str(os.popen("egrep 'hidden=' /etc/NetworkManager/system-connections/" + ssid).read())
if hidden.find('true'):
	hidden = 'True'
else:
	hidden = 'False'
key = str(os.popen("egrep 'key-mgmt=' /etc/NetworkManager/system-connections/" + ssid).read())
if key.find('wpa'):
	key = 'WPA'
elif key.find('ieee8021x'):
	key = 'WEP'
else:
	key = 'nopass'
psk = str(os.popen("egrep 'psk=' /etc/NetworkManager/system-connections/" + ssid).read())
psk = psk[4:-1]
qr_text = 'WIFI:S:'+ssid+';T:'+key+';P:'+psk+';H:'+hidden+';;'
qr = qrcode.QRCode()
qr.add_data(qr_text)
qr.print_ascii()
print('    Wi-Fi Name: '+ssid+'\n')
