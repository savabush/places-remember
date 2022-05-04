from django.test import SimpleTestCase
from .. import forms


class TestForms(SimpleTestCase):

    def test_memory_form_valid_data(self):
        form = forms.MemoryForm(data={
            'name': 'Town',
            'comment': 'Some comment'
        })

        self.assertTrue(form.is_valid())

    def test_memory_form_no_data(self):
        form = forms.MemoryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
