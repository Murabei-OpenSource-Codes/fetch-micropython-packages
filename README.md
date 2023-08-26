# Fetch Micropython Packages
This package was created to help installing packages on ESP32 boards using
Micropython python.

mremote and mpip are dificult to use and need the board to be connected to
a WiFi network. mfetch download packages avaiable on git repository and
save them on packages/ folder. This folder can later be copied to ESP32
lib/ folder at board build process.

This is much easier since the board is ready for use after installing the
codes and packages.

## Example of use
