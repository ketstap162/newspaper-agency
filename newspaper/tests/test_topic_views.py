from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic

TOPICS_URL = reverse("newspaper:topic-list")


class TopicViewTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="test123user"
        )
        self.client.force_login(self.redactor)

    def test_retrieve_topics(self):
        Topic.objects.create(
            name="Topic1",
        )
        Topic.objects.create(
            name="Topic2",
        )

        topics = Topic.objects.all()

        response = self.client.get(TOPICS_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")
