"""Faz o led da placa piscar."""
import machine
import time
from wifi_setup_server.server import WifiSetupServer

# Internet connection Status PIN
pin_board = machine.Pin(2, machine.Pin.OUT)
pin_red = machine.Pin(15, machine.Pin.OUT)
pin_yellow = machine.Pin(12, machine.Pin.OUT)
pin_green = machine.Pin(13, machine.Pin.OUT)

# Clean board pins
internet_object = WifiSetupServer(
    config_server_pin=pin_red,
    connecting_wifi_pin=pin_yellow,
    connected_wifi_pin=pin_green)


def main():
    """Start function to the board."""
    board_id = internet_object.get_board_id()
    while True:
        print("board_id:", board_id)
        internet_object.configure_wifi()
        time.sleep(1)
