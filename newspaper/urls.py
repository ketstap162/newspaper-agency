from django.urls import path

from newspaper.views import index, TopicListView, NewspaperListView, RedactorListView, NewspaperDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
]

app_name = "newspaper"
