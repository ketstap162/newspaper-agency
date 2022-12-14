from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"
        ordering = ["id"]

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.username} ({self.first_name} {self.last_name})"
        return self.username


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    published_date = models.DateField(null=True)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
