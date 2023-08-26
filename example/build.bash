export MICROPYTHON_PACKAGES="../../micropython-lib/micropython"

echo -e "# Clean board files:"
ampy --port /dev/ttyUSB0 rmdir /lib
ampy --port /dev/ttyUSB0 rmdir /code
ampy --port /dev/ttyUSB0 mkdir /lib

echo -e "# List config files:"
ampy --port /dev/ttyUSB0 ls /config
# ampy --port /dev/ttyUSB0 rm /config/wifi_credentials.json

echo -e "# Install packages:"
echo -e "## Requirements"
ampy --port /dev/ttyUSB0 put ./lib

echo -e "## Packages"
ampy --port /dev/ttyUSB0 put $MICROPYTHON_PACKAGES/urequests /lib/urequests
ampy --port /dev/ttyUSB0 ls /lib/


echo -e "# Pushing boot:"
ampy --port /dev/ttyUSB0 put ./boot/boot.py boot.py
ampy --port /dev/ttyUSB0 ls ./

echo -e "\n# Pushing code:"
ampy --port /dev/ttyUSB0 put ./code
ampy --port /dev/ttyUSB0 ls ./code

ampy --port /dev/ttyUSB0 reset
