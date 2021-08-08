#
# Run INIT RAM STATIC
# Test of command INIT_RAM_STATIC

import sys
from uart_max7219_ctrl_class import *




uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)
uart_rpi.init_static_ram()
uart_rpi.close_uart()
