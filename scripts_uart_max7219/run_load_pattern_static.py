#
# run_load_pattern_static
# Run LOAD_PATTERN_STATIC Command and check


import sys
import numpy as np

from uart_max7219_ctrl_class import *


start_ptr = int(sys.argv[1])


uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)

# Send data : Byte(0) = Start @
# Bytes(1-128) = data



# Data Array creation
matrix_line = []
matrix = []
for j in range(0, 8):
    matrix_line = []
    for i in range(0, 64):
        matrix_line.append(1)
    matrix.append(matrix_line)

matrix_array = np.array(matrix)

print(matrix_array)

static_pattern_data = uart_rpi.matrix_2_static_pattern(matrix_array)

print("static_pattern_data : %s" %(static_pattern_data) )

print("len(static_pattern_data) : %d" %(len(static_pattern_data)) )
    
uart_rpi.load_pattern_static(start_ptr, static_pattern_data)
uart_rpi.close_uart()
