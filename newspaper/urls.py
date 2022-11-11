from django.urls import path

from newspaper.views import index


urlpatterns = [
    path("", index, name="index"),
]

app_name = "newspaper"
