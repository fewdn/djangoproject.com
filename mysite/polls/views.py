from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response_msg = "Hello, world. You're at the polls index." \
                   f"You made a {request.method} request." \
                   f"The server is running on port {request.META['SERVER_PORT']}."
    return HttpResponse(response_msg)