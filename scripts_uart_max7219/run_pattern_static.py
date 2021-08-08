#
# run_pattern_static
# Run RUN_PATTERN_STATIC Command and check


import sys
from uart_max7219_ctrl_class import *



start_ptr = int(sys.argv[1])
last_ptr  = int(sys.argv[2])

uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)

print("start_ptr : %d  last_ptr : %d" %(start_ptr, last_ptr) )
    
uart_rpi.run_pattern_static(start_ptr, last_ptr)
uart_rpi.close_uart()
