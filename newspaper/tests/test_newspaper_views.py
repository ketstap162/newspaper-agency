from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper

NEWSPAPERS_URL = reverse("newspaper:newspaper-list")


class NewspaperViewsTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="test123user"
        )
        self.client.force_login(self.redactor)

        topic1 = Topic.objects.create(
            name="Manufname1",
        )
        topic2 = Topic.objects.create(
            name="Manufname2",
        )

        self.newspaper1 = Newspaper.objects.create(
            title="News1",
            topic=topic1
        )
        self.newspaper2 = Newspaper.objects.create(
            title="News2",
            topic=topic2
        )

    def test_retrieve_newspapers(self):
        newspapers = Newspaper.objects.all()

        response = self.client.get(NEWSPAPERS_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")

    def test_newspaper_listed(self):
        response = self.client.get(NEWSPAPERS_URL)

        self.assertContains(response, self.newspaper1.id)
        self.assertContains(response, self.newspaper1.title)
        self.assertContains(response, self.newspaper1.topic)
        self.assertContains(response, self.newspaper2.id)
        self.assertContains(response, self.newspaper2.title)
        self.assertContains(response, self.newspaper2.topic)
