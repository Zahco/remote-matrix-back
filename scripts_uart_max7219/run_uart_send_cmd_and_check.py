#
# Run UART_SEND_CMD_AND_CHECK function
# Send a custom command and check

import sys
from uart_max7219_ctrl_class import *

data_2_send       = sys.argv[1]
data_2_check_size = int(sys.argv[3])

if(len(sys.argv[2]) < data_2_check_size):
    null_car_concat = ""
    for i in range(0, (data_2_check_size - len(sys.argv[2]))):
        null_car_concat = null_car_concat + '\0' 
   
    data_2_check      = sys.argv[2] + null_car_concat

#print("DEBUG - data_2_check : %s" %(data_2_check) )

uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)
uart_rpi.uart_send_cmd_and_check(data_2_send, data_2_check, data_2_check_size)
uart_rpi.close_uart()
