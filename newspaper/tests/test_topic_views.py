from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic

TOPICS_URL = reverse("newspaper:topic-list")


class TopicViewTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="test123user",
            is_staff=True,
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

    def test_search_topics_by_name(self):
        search_word = "C"
        topics_names = ["Crime", "Cultural", "Military", "Music"]

        for name in topics_names:
            Topic.objects.create(
                name=name,
            )

        payload = {
            "search_by": search_word
        }

        response = self.client.get(TOPICS_URL, data=payload)

        for name in [
            word for word in topics_names
            if search_word.lower() in word.lower()
        ]:
            self.assertContains(response, name)

        for name in [
            word for word in topics_names
            if search_word.lower() not in word.lower()
        ]:
            self.assertNotContains(response, name)

    def test_topic_update(self):
        topic = Topic.objects.create(
            name="FirstTestTopicName"
        )

        self.client.post(
            reverse("newspaper:topic-update", args=[topic.id]),
            data={"name": "SecondTestTopicName"}
        )

        topic.refresh_from_db()

        self.assertEqual(topic.name, "SecondTestTopicName")
