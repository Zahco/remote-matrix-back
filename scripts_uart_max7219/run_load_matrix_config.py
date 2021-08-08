#
# run_load_matrix_config.py
# Test of function LOAD MATRIX CONFIG

import sys
from uart_max7219_ctrl_class import *



DISPLAY_TEST = sys.argv[1]
DECODE_MODE  = sys.argv[2]
SCAN_LIMIT   = sys.argv[3]
INTENSITY    = sys.argv[4]
SHUTDOWN     = sys.argv[5]

uart_rpi  = uart_max7219_ctrl_class(baudrate = 230400)
uart_rpi.load_matrix_config(DISPLAY_TEST, DECODE_MODE, SCAN_LIMIT, INTENSITY, SHUTDOWN)
uart_rpi.close_uart()
