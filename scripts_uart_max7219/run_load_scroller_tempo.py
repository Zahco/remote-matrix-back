#
# run_load_scroller_tempo.py
# Test of function LOAD SCROLLER TEMPO

import sys
from uart_max7219_ctrl_class import *



DATA_TEMPO = int(sys.argv[1], 16)

print("DATA_TEMPO : %d - 0x%x" %(DATA_TEMPO, DATA_TEMPO) )

uart_rpi  = uart_max7219_ctrl_class(baudrate = 230400)
uart_rpi.run_load_scroller_tempo(DATA_TEMPO)
uart_rpi.close_uart()
