#
# run_pattern_scroller
# Run RUN_PATTERN_SCROLLER Command and check


import sys
from uart_max7219_ctrl_class import *



start_ptr  = int(sys.argv[1])
msg_length = int(sys.argv[2])

uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)

print("start_ptr : %d  msg_length : %d" %(start_ptr, msg_length) )
    
uart_rpi.run_pattern_scroller(start_ptr, msg_length)
uart_rpi.close_uart()
