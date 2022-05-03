from core.handlers import vk_access_token
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import MemoryForm
from .models import Memory
import re
import secret


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                mapbox_key = secret.mapbox_key
                vk_token = vk_access_token.get_access_token(request)[0]
                owner_id = vk_access_token.get_access_token(request)[1]
                memories_user = User.objects.get(id=request.user.id).memories.all()
                return render(request, 'core/index.html', {'vk_access_token': vk_token,
                                                           'owner_id_vk': owner_id,
                                                           'memories': memories_user,
                                                           'mapbox_key': mapbox_key,
                                                           })
        return render(request, 'core/index.html')

    def post(self, request):
        mapbox_key = secret.mapbox_key
        id_memory = list(request.POST)[1]
        Memory.objects.get(id=id_memory).delete()
        vk_token = vk_access_token.get_access_token(request)[0]
        owner_id = vk_access_token.get_access_token(request)[1]
        memories_user = User.objects.get(id=request.user.id).memories.all()
        return render(request, 'core/index.html', {'vk_access_token': vk_token,
                                                   'owner_id_vk': owner_id,
                                                   'memories': memories_user,
                                                   'mapbox_key': mapbox_key,
                                                   })


class AddMemory(View):
    form_class = MemoryForm
    mapbox_key = secret.mapbox_key

    def get(self, request):
        form = self.form_class()
        return render(request, 'core/addmemory.html', {'mapbox_key': self.mapbox_key, 'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            points = re.findall(r'[0-9-\.0-9]+', request.GET.get('points'))
            point_lng = points[0]
            point_lat = points[1]
            author = User.objects.get(id=request.user.id)
            Memory.objects.create(**form.cleaned_data, author=author, point_lng=point_lng, point_lat=point_lat)
            return redirect('/')
        return render(request, 'core/addmemory.html', {'mapbox_key': self.mapbox_key, 'form': form})