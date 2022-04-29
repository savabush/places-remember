from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.Index.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('addmemory/', views.AddMemory.as_view(), name='addmemory')
]
