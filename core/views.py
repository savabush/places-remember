from django.shortcuts import render
from django.views import View
import secret


def index(request):
    return render(request, 'core/index.html')


class AddMemory(View):
    def get(self, request):
        mapbox_key = secret.mapbox_key
        return render(request, 'core/addmemory.html', {'mapbox_key': mapbox_key})

    def post(self, request):
        pass
