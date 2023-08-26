"""This file is executed on every boot (including wake-boot from deepsleep)."""
import uos, machine
import gc
from code.main import main

gc.collect()
main()
