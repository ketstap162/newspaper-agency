from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper

REDACTORS_URL = reverse("newspaper:redactor-list")


class RedactorViewsTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="test-user",
            password="test123user"
        )

        self.client.force_login(self.redactor)

    def test_retrieve_redactors(self):
        redactors = get_user_model().objects.all()

        response = self.client.get(REDACTORS_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")

    def test_redactor_listed(self):
        self.redactor.years_of_experience = 4
        self.redactor.first_name = "Bobik"
        self.redactor.last_name = "Sdoh"
        self.redactor.save()

        response = self.client.get(REDACTORS_URL)

        for value in [
            self.redactor.id,
            self.redactor.username,
            self.redactor.first_name,
            self.redactor.last_name,
            self.redactor.years_of_experience
        ]:
            self.assertContains(response, value)
