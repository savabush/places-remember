from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .. import models


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('test_user')
        author = User.objects.get(username='test_user')
        for x in range(15):
            self.project1 = models.Memory.objects.create(
                author=author,
                name=f'Town{x}',
                comment=f'Some comment{x * x}',
                point_lng='50',
                point_lat='50'
            )

    def test_index_get(self):
        response = self.client.get(reverse('index'))

        self.assertURLEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertEquals(models.Memory.objects.all().count(), 15)

    def test_index_post(self):
        object_of_model = models.Memory.objects.get(name='Town1')
        object_of_model.delete()
        self.assertEquals(models.Memory.objects.all().count(), 14)

    def test_addmemory_nolog_get(self):
        response = self.client.get(reverse('addmemory'))
        self.assertURLEqual(response.status_code, 302)
