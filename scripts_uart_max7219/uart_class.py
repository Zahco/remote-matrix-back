#
# Class for UART management by RPi
#
#

import sys
import serial
import time



class uart_class:

    # Constructor
    def __init__(self, baudrate = 9600, timeout = 0, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE):
        self.baudrate = baudrate
        self.timeout  = timeout
        self.bytesize = bytesize
        self.parity   = parity
        self.stopbits = stopbits
        self.com_uart = serial.Serial("/dev/ttyAMA0")
        print("UART Com. OPEN !")


    # Init UART communication
    def init_uart_com(self):
        self.com_uart.baudrate = self.baudrate
        self.com_uart.timeout  = self.timeout
        self.com_uart.bytesize = self.bytesize
        self.com_uart.parity   = self.parity
        self.com_uart.stopbits = self.stopbits
        print("INIT_UART_COM Done !")
        

    # Open UART communication
    def open_uart_com(self):
        self.com_uart.open()
        print("UART Com. OPEN !")



    # Close UART communication
    def close_uart_com(self):
        self.com_uart.close()
        print("UART Com. CLOSE !")


    # Write Data from UART
    def uart_write_data(self, data):
        self.com_uart.write(data)

    # Read Data from UART - Print in console 
    def uart_read_data(self, nb_data):
        data_2_read = self.com_uart.read(nb_data)
        print("UART received data : %s" %(data_2_read) )
