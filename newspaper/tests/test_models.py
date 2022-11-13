from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper, Redactor


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Lol kek 221",
        )
        self.assertEqual(
            str(topic),
            "Lol kek 221"
        )

    def test_redactor_is_user_class(self):
        self.assertIs(Redactor, get_user_model())

    def test_redactor_str_without_full_name(self):
        redactor = get_user_model().objects.create_user(
            username="usercheck",
            password="checker123",
        )
        self.assertEqual(
            str(redactor),
            "usercheck"
        )

    def test_redactor_str_with_full_name(self):
        redactor = get_user_model().objects.create_user(
            username="usercheck2",
            password="checker1232",
            first_name="Lol",
            last_name="Kek",
        )
        self.assertEqual(
            str(redactor),
            "usercheck2 (Lol Kek)"
        )


    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="TopIk",

        )

        newspaper = Newspaper.objects.create(
            title="SuperNews",
            content="Super super super news",
            topic=topic,
        )

        self.assertEqual(
            str(newspaper),
            "SuperNews"
        )
