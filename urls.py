from django.urls import path, include
from remotematrixapi.controllers import ping, matrix
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('ping', ping.getPing),
    path('matrix/state', matrix.state),
    path('matrix/reset', matrix.reset)
]
urlpatterns = format_suffix_patterns(urlpatterns)