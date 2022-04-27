from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=150)
    photo = models.URLField(default=None)

    class Meta:
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'

    def __str__(self):
        return f'Name - {self.name}'
