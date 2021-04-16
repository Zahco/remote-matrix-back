from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def state(request):
    if request.method == 'GET':
        # TODO get matrix state
        return Response({ 'state': [] })
    elif request.method == 'POST':
        # TODO Apply update matrix
        return Response({ 'state': request.POST.get('test') })