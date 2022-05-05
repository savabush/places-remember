from core.handlers import vk_access_token
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import MemoryForm
from .models import Memory
import re
import secret


class Index(ListView):
    model = Memory
    template_name = 'core/index.html'
    context_object_name = 'memories'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            if not self.request.user.is_superuser:
                context = super().get_context_data()
                context['vk_access_token'] = vk_access_token.get_access_token(self.request)[0]
                context['owner_id_vk'] = vk_access_token.get_access_token(self.request)[1]
                context['mapbox_key'] = secret.mapbox_key
                return context
        context = super().get_context_data()
        return context

    def post(self, request):
        id_memory = list(request.POST)[1]
        Memory.objects.get(id=id_memory).delete()
        return redirect('/')


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