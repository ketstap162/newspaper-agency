from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorListView,
    NewspaperDetailView,
    RedactorDetailView,
    TopicDetailView, RedactorCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topic/<int:pk>/",
        TopicDetailView.as_view(),
        name="topic-detail"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
]

app_name = "newspaper"
