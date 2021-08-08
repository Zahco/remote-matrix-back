from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
import json


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def state(request):
    if request.method == 'GET':
        # TODO get matrix state
        return Response({ 'state': [] })
    elif request.method == 'POST':
        # TODO Apply update matrix
        return Response({ 'body': request.body.json() })
        # return Response({ 'body': json.loads(request.body.decode('utf-8')) })
        # matrix = json.loads(request.body)['matrix']
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         matrix[i][j] = int(matrix[i][j])
        # array = []
        # for line in matrix:
        #     array += line
        # return Response({ 'matrix': matrix, 'line': array })