
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the new home.")

def about(request):
    return HttpResponse("Hello, world. You're at the new about.")