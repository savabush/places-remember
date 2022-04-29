from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from core.handlers import vk_access_token
import secret


def index(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            vk_token = vk_access_token.get_access_token(request)[0]
            owner_id = vk_access_token.get_access_token(request)[1]
            memories_user = User.objects.get(id=request.user.id).memories.all()
            return render(request, 'core/index.html', {'vk_access_token': vk_token,
                                                       'owner_id_vk': owner_id,
                                                       'memories': memories_user})
    return render(request, 'core/index.html')


class AddMemory(View):
    def get(self, request):
        mapbox_key = secret.mapbox_key
        return render(request, 'core/addmemory.html', {'mapbox_key': mapbox_key})

    def post(self, request):
        print(request)
        return index(request)
