from django.shortcuts import render
from .models import Server

# Create your views here.


def state(request):
    servers = Server.objects.all()
    return render(request, 'web/state.html', locals())
