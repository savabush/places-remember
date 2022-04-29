from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memories')
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=150)
    point_lng = models.CharField(max_length=20, default=0)
    point_lat = models.CharField(max_length=20, default=0)

    class Meta:
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'

    def __str__(self):
        return f'Author - {self.author}, name - {self.name}'