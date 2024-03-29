# 3G/4G LTE Weather Station
GPRS for Davis Weather Station using a Beaglebone Black and Debian custom firmware (kernel supports standby).

The project is for my local paragliding club to setup a Davis Weather in a remote location with internet access.

Hardware:
---------
* Davis Vantage Pro2 Wireless Weather Station (6152)
* Davis Complete System Shelter for all weather station components (7724)
* Davis USB Data Logger
* Beaglebone Black
* USB to Serial cable FTDI TTL-232R-3V3 (optional)
* USB A micro cable
* USB A mini cable
* USB (optional powered) hub (Belkin Ultra Slim 4 Port USB powered hub 5v input)
* Huawei 3G modem (E3531)
* 3G/4G SIM card
* Sunix 10A 12V/24V Solar Charge Regulator
* 20W 12V Photonic Universe solar panel
* 12v 7ah Sealed Lead Acid Rechargeable Battery
* ELP 2MP Full HD Night Vision H.264 Webcam Bullet Waterproof 30fps MJPEG USB Camera (optional)
* INA219 I2C Module Bidirectional DC Current Power Monitoring (optional)
  
Software:
---------
* Debian custom firmware bone-debian-9.2-console-armhf-2017-12-08-2gb.img.xz
* [WeeWX](http://www.weewx.com/) open source weather software
