from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
import json
import sys
from remotematrixapi.scripts_uart_max7219.uart_max7219_ctrl_class import *
import numpy as np





@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def state(request):
    if request.method == 'GET':
        # TODO get matrix state
        return Response({ 'state': [] })
    elif request.method == 'POST':
        # TODO Apply update matrix
        matrix = json.loads(request.body.decode('utf-8'))['matrix']
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])

        # jorisclass.sendmatrix(matrix)
        uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)
        matrix_array = np.array(matrix)
        static_pattern_data = uart_rpi.matrix_2_static_pattern(matrix_array)
        uart_rpi.load_pattern_static(start_ptr, static_pattern_data)
        uart_rpi.close_uart()
        return Response({ 'matrix': matrix })

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def reset(request):
    if request.method == 'POST':
        uart_rpi = uart_max7219_ctrl_class(baudrate = 230400)
        uart_rpi.init_static_ram()
        uart_rpi.close_uart()
        return Response({ 'msg': 'success' })