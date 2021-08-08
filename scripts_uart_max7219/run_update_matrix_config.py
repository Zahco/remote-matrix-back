#
# Run UPDATE MATRIX CONFIG Function
# Test of UPDATE MATRIX CONFIG Command

from uart_max7219_ctrl_class import *

uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)
uart_rpi.update_matrix_config()
uart_rpi.close_uart()
