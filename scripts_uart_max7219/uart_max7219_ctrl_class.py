#
# uart_max729_ctrl_class.py
#

import sys
import numpy as np

from uart_class import *



class uart_max7219_ctrl_class:

    # ===============
    # == CONSTANTS ==
    # ===============

    UART_CMD = dict()
    UART_CMD["INIT_RAM_STATIC"]      = "INIT_RAM_STATIC\0\0\0\0\0"
    UART_CMD["INIT_RAM_SCROLLER"]    = "INIT_RAM_SCROLLER\0\0\0"
    UART_CMD["UPDATE_MATRIX_CONFIG"] = "UPDATE_MATRIX_CONFIG"
    UART_CMD["LOAD_MATRIX_CONFIG"]   = "LOAD_MATRIX_CONFIG\0\0"
    UART_CMD["LOAD_PATTERN_STATIC"]  = "LOAD_PATTERN_STATIC\0"
    UART_CMD["LOAD_PATTERN_SCROLL"]  = "LOAD_PATTERN_SCROLL\0"
    UART_CMD["RUN_PATTERN_STATIC"]   = "RUN_PATTERN_STATIC\0\0"
    UART_CMD["RUN_PATTERN_SCROLLER"] = "RUN_PATTERN_SCROLLER"
    UART_CMD["LOAD_SCROLLER_TEMPO"]  = "LOAD_SCROLLER_TEMPO\0"

    UART_RESP = dict()
    UART_RESP["RAM_STATIC_DONE"]     = "RAM_STATIC_DONE\0\0\0\0\0"
    UART_RESP["RAM_SCROLLER_DONE"]   = "RAM_SCROLLER_DONE\0\0\0"
    UART_RESP["CMD_DISCARD"]         = "CMD_DISCARD\0\0\0\0\0\0\0\0\0"
    UART_RESP["LOAD_STATIC_RDY"]     = "LOAD_STATIC_RDY\0\0\0\0\0"
    UART_RESP["LOAD_STATIC_NOT_RDY"] = "LOAD_STATIC_NOT_RDY\0"
    UART_RESP["LOAD_STATIC_DONE"]    = "LOAD_STATIC_DONE\0\0\0\0"
    UART_RESP["LOAD_SCROLL_RDY"]     = "LOAD_SCROLL_RDY\0\0\0\0\0"
    UART_RESP["LOAD_SCROLL_NOT_RDY"] = "LOAD_SCROLL_NOT_RDY\0"
    UART_RESP["LOAD_SCROLL_DONE"]    = "LOAD_SCROLL_DONE\0\0\0\0"
    UART_RESP["LOAD_MATRIX_RDY"]     = "LOAD_MATRIX_RDY\0\0\0\0\0"
    UART_RESP["LOAD_MATRIX_DONE"]    = "LOAD_MATRIX_DONE\0\0\0\0"
    UART_RESP["UPDATE_MATRIX_DONE"]  = "UPDATE_MATRIX_DONE\0\0"
    UART_RESP["STATIC_PTRN_RDY"]     = "STATIC_PTRN_RDY\0\0\0\0\0"
    UART_RESP["STATIC_PTRN_NOT_RDY"] = "STATIC_PTRN_NOT_RDY\0"
    UART_RESP["STATIC_PTRN_DONE"]    = "STATIC_PTRN_DONE\0\0\0\0"
    UART_RESP["SCROLL_PTRN_RDY"]     = "SCROLL_PTRN_RDY\0\0\0\0\0"
    UART_RESP["SCROLL_PTRN_NOT_RDY"] = "SCROLL_PTRN_NOT_RDY\0"
    UART_RESP["SCROLL_PTRN_DONE"]    = "SCROLL_PTRN_DONE\0\0\0\0"
    UART_RESP["LOAD_TEMPO_RDY"]      = "LOAD_TEMPO_RDY\0\0\0\0\0\0"
    UART_RESP["LOAD_TEMPO_NOT_RDY"]  = "LOAD_TEMPO_NOT_RDY\0"
    UART_RESP["LOAD_TEMPO_DONE"]     = "LOAD_TEMPO_DONE\0\0\0\0\0"

    # Config. Matrix Registers
    DISPLAY_TEST = 0
    DECODE_MODE  = 0x00
    SCAN_LIMIT   = 0x00
    INTENSITY    = 0x00
    SHUTDOWN     = 0x00


    # TESTS PATTERNS
    test_pattern_ones = np.ones((8, 63), int)

    
    # ================
    # == CONSTUCTOR ==
    # ================

    # Constructor
    def __init__(self,
                 baudrate = 9600,
                 timeout  = 1,
                 bytesize = serial.EIGHTBITS,
                 parity   = serial.PARITY_NONE,
                 stopbits = serial.STOPBITS_ONE):
        
        self.uart_inst = uart_class(baudrate, timeout, bytesize, parity, stopbits)
        self.uart_inst.init_uart_com()

        # debug
        # print(type(self.UART_CMD["RUN_PATTERN_SCROLLER"]))
        

        # ========================
        # == UART RPi FUNCTIONS ==
        # ========================

    # Start a command and wait check response
    # Default Size of response : 20 bytes
    def uart_send_cmd_and_check(self, data_2_send, data_2_check, data_2_check_size = 20):
        check = False
        self.uart_inst.uart_write_data(data_2_send)
        read_data = self.uart_inst.com_uart.read_until(data_2_check, data_2_check_size)
        if (len(read_data) < data_2_check_size):
            print("Error a Timeout occurs - Not enough data - Number of data Received %d data : expected %d" %(len(read_data), data_2_check_size) )
            check = False
        else:
            if(read_data == data_2_check):
                print("Received Data : %s - expected : %s => OK" %(read_data, data_2_check) )
                check = True
            else:
                print("Received Data : %s - expected : %s => ERROR" %(read_data, data_2_check) )
                check = False

        return check



    # INIT_STATIC_RAM command
    def init_static_ram(self):
        check = self.uart_send_cmd_and_check(self.UART_CMD["INIT_RAM_STATIC"], self.UART_RESP["RAM_STATIC_DONE"])


    # INIT_SCROLLER_RAM command
    def init_scroll_ram(self):
        check = self.uart_send_cmd_and_check(self.UART_CMD["INIT_RAM_SCROLLER"], self.UART_RESP["RAM_SCROLLER_DONE"])

    

    # LOAD MATRIX CONFIG
    def load_matrix_config(self, DISPLAY_TEST, DECODE_MODE, SCAN_LIMIT, INTENSITY, SHUTDOWN):

        # Send LOAD_MATRIX_CONFIG and check result
        check = self.uart_send_cmd_and_check(self.UART_CMD["LOAD_MATRIX_CONFIG"], self.UART_RESP["LOAD_MATRIX_RDY"])

        # Send DAta and check
        if(check == True):
            print("LOAD_MATRIX_RDY received !")
            matrix_config_data = DISPLAY_TEST + DECODE_MODE + SCAN_LIMIT + INTENSITY + SHUTDOWN
            check = self.uart_send_cmd_and_check(matrix_config_data, self.UART_RESP["LOAD_MATRIX_DONE"])
        else:
            print("Abort LOAD_MATRIX_CONFIG - Display controller NOT READY")


    # UPDATE MATRIX CONFIG
    def update_matrix_config(self):

        # Send UPDATE_MATRIX_CONFIG and check result
        check = self.uart_send_cmd_and_check(self.UART_CMD["UPDATE_MATRIX_CONFIG"], self.UART_RESP["UPDATE_MATRIX_DONE"])

        if(check == True):
            print("UPDATE_MATRIX_DONE received !")
        else:
            print("UPDATE_MATRIX_CONFIG Error !")




    # LOAD PATTERN STATIC
    # pattern_static_data
    # Data to send : Byte(0) = Start @
    # Byte(1)    => Byte(128) = DAta to load in RAM
    # Byte(odd)  = MSB[15:8] of RAM DATA
    # Byte(even) = LSB[7:0] of RAM DATA
    def load_pattern_static(self, start_ptr, pattern_static_data):

        # Send LOAD_PATTERN_STATIC command and check if FPGA is ready
        check = self.uart_send_cmd_and_check(self.UART_CMD["LOAD_PATTERN_STATIC"], self.UART_RESP["LOAD_STATIC_RDY"])

        
        if(check == True):
            print("LOAD_STATIC_RDY received !")

            data_int_tmp = []
            # Convert Integer array list to Byte data to send by UART
            print("len(pattern_static_data) : %d" %(len(pattern_static_data)))

            # Convert Data Matrix on 16bits to Data on 8 bits
            for i in range(0, len(pattern_static_data)):
                #data_int_tmp.append(pattern_static_data[i] & 0xFF)
                data_int_tmp.append((pattern_static_data[i] >> 8) & 0xFF)
                data_int_tmp.append(pattern_static_data[i] & 0xFF)

            # Convert Data int 8 bit to STR
            data_tmp = ""
            for i in range(0, len(data_int_tmp)):
                data_tmp = data_tmp + str(format(data_int_tmp[i], "02x"))
                
            data_to_send = ""
            data_to_send = str(format(start_ptr, "02x")) + data_tmp

            data_to_send = bytearray.fromhex(data_to_send)
            print("data_to_send : %s -  len(data_to_send) : %d" %(data_to_send, len(data_to_send)) )
            
            # Send Load STATIC Pattern
            check = self.uart_send_cmd_and_check(data_to_send, self.UART_RESP["LOAD_STATIC_DONE"])

            if(check == True):
                print("LOAD_STATIC_DONE reveived !")
            else:
                print("LOAD_STATIC_PATTERN Error !")
                
        else:
            print("LOAD_PATTERN_STATIC Error !")

            
    # RUN PATTERN STATIC
    # start_ptr/last_ptr = integer in hexa on 8 bits
    def run_pattern_static(self, start_ptr, last_ptr):
        check = self.uart_send_cmd_and_check(self.UART_CMD["RUN_PATTERN_STATIC"], self.UART_RESP["STATIC_PTRN_RDY"])

        if(check == True):
            print("STATIC_PTRN_RDY received !")

            # Convert start_ptr and last_ptr
            data_tmp            = str(format(start_ptr, "02x")) + str(format(last_ptr, "02x"))
            data_to_send = bytearray.fromhex(data_tmp)
            
            check = self.uart_send_cmd_and_check(data_to_send, self.UART_RESP["STATIC_PTRN_DONE"])
            
            if(check == True):
                print("STATIC_PTRN_DONE received !")
            else:
                print("LOAD START AND LAST PTR STATIC Error !")
                
        else:
            print("RUN_PATTERN_STATIC Error !")





    # LOAD PATTERN SCROLLER
    # start_ptr = An integer on 8 bits
    # msg_length = An integer on 8 bits
    # pattern_scroller_data : A list with Dater per Digit
    def load_pattern_scroller(self, start_ptr, msg_length, pattern_scroller_data):

        check = self.uart_send_cmd_and_check(self.UART_CMD["LOAD_PATTERN_SCROLL"], self.UART_RESP["LOAD_SCROLL_RDY"])

        
        if(check == True):
            print("LOAD_SCROLL_RDY received !")

            # Start PTR and MSG length to STR
            data_tmp = str(format(start_ptr, "02x")) + str(format(msg_length, "02x"))

            # Convert PAttern scroller to a STR
            data_int_tmp = ""
            for i in range(0, len(pattern_scroller_data)):
                data_int_tmp = data_int_tmp + str(format(pattern_scroller_data[i], "02x"))


            # Convert all data to UART format
            pattern_scroll_data = bytearray.fromhex(data_tmp) + bytearray.fromhex(data_int_tmp)
            print("len(pattern_scroll_data) : %d" %(len(pattern_scroll_data)) )
            
            check = self.uart_send_cmd_and_check(pattern_scroll_data, self.UART_RESP["LOAD_SCROLL_DONE"])

            if(check == True):
                print("LOAD_SCROLL_DONE received !")
            else:
                print("LOAD START PTR AND MSG LENGTH Error !")

        else:
            print("LOAD_PATTERN_SCROLL Error !")


    # RUN PATTERN SCROLLER
    def run_pattern_scroller(self, start_ptr, msg_length):

        check = self.uart_send_cmd_and_check(self.UART_CMD["RUN_PATTERN_SCROLLER"], self.UART_RESP["SCROLL_PTRN_RDY"])

        if(check == True):
            print("SCROLL_PTRN_DONE received !")
            

            data_tmp = str(format(start_ptr, "02x")) + str(format(msg_length, "02x"))
            run_data = bytearray.fromhex(data_tmp)

            check = self.uart_send_cmd_and_check(run_data, self.UART_RESP["SCROLL_PTRN_DONE"])

            if(check == True):
                print("SCROLL_PTRN_DONE received !")
            else:
                print("Run PATTERN SCROLLER Error !")

        else:
            print("RUN PATTERN SCROLLER Error !")


    # Run LOAD_SCROLLER_TEMPO
    # DAta_tempo : an integer on 32 bits
    def run_load_scroller_tempo(self, data_tempo):
        check = self.uart_send_cmd_and_check(self.UART_CMD["LOAD_SCROLLER_TEMPO"], self.UART_RESP["LOAD_TEMPO_RDY"])

        if(check == True):
            print("LOAD_TEMPO_RDY received !")
            
            data_tmp = str(format( (data_tempo >> 24) & 0xFF , "02x")) + str(format( (data_tempo >> 16) & 0xFF , "02x"))  
            data_tmp = data_tmp + str(format( (data_tempo >> 8) & 0xFF , "02x")) + str(format( (data_tempo) & 0xFF , "02x"))  

            print("data_tmp : %s" %(data_tmp) )
            run_data = bytearray.fromhex(data_tmp)
            print("DEBUG - run_data : %s" %(run_data))
            check    = self.uart_send_cmd_and_check(run_data, self.UART_RESP["LOAD_TEMPO_DONE"])

            if(check == True):
                print("LOAD_TEMPO_DONE received !")
            else:
                print("LOAD_TEMPO_DONE Error !")
        else:
            print("RUN LOAD_SCROLLER_TEMPO Error !")

            
    # Resynch. UART communication
    # Send Data until the reception of CMD_DISCARD respons
    def resynch_com_uart(self):

        resynch_done = False
        while (resynch_done == False):
            check = self.uart_send_cmd_and_check("0", SELF.UART_RESP["CMD_DISCARD"])
            if(check == True):
                print("CMD_DISCARD received -  Resynchronization done !")
                resynch_done = True

                
                
    # Close UART
    def close_uart(self):
        self.uart_inst.close_uart_com()



    # ====================
    # == MISC FUNCTIONS ==
    # ====================


    # A Matrix Array 8*63 to STATIC Pattern data
    # matrix_array : np object 8 Raws  63 Columns
    #
    # Output :
    #         * static_pattern_ram_data - A list of data to write in RAM in integer
    #  
    def matrix_2_static_pattern(self, matrix_array):
        
        static_pattern_ram_data = []
        data_list = self.matrix_2_data_list(matrix_array)

        # Digit Sel
        for i in range(0, 8):

            # Matrix Sel
            for j in range(0, 8):

                if(j < 7):
                    static_pattern_ram_data.append( ((i + 1) << 8) | data_list[63 - 8*j - i])

                # For 8th Matrix add En
                else:
                    static_pattern_ram_data.append( (1 << 12) | ((i + 1) << 8) | data_list[63 - 8*j - i])

        return static_pattern_ram_data

        
    # A matrix of 8*63
    # Return a list of Bytes
    # data_list[0] = Digit(7)(M0)
    # data_list[1] = Digit(6)(M0)
    # ...
    # data_list[63] = Digit(0)(M7)
    def matrix_2_data_list(self, matrix_array):

        data_list = []
        for i in range(0, 64):
            data_tmp = ""
            for j in range(0, 8):
                data_tmp = data_tmp + str(matrix_array[j][i])

            data_list.append(int(data_tmp, 2))

        return data_list
        

    
    # ===========
    # == DEBUG ==
    # ===========
    
    # DEBUG
    def display_tests_patterns(self):
        print(self.test_pattern_ones)


        
