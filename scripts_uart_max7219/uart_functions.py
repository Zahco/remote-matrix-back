#
# Function for UART test
#

import sys
import serial
import time


from uart_class import *

def uart_self_test(data_to_send):

    uart_inst = uart_class(baudrate = 2*115200)

    uart_inst.init_uart_com()
#    uart_inst.open_uart_com()
    uart_inst.uart_write_data(data_to_send)
    time.sleep(0.01)
    uart_inst.uart_read_data(len(data_to_send))
    uart_inst.close_uart_com()



# Main test
data_to_send = sys.argv[1]

uart_self_test(data_to_send)
