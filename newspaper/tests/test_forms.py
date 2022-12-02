from django.test import TestCase

from newspaper.forms import RedactorCreationForm


class FormTests(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "newuser",
            "password1": "u123test",
            "password2": "u123test",
            "first_name": "Nametest",
            "last_name": "Surnametest",
            "years_of_experience": 3
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
        self.assertEqual(form.fields.keys(), form_data.keys())
