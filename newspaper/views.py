from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorCreationForm, RedactorYearsUpdateForm
from newspaper.models import Redactor, Newspaper, Topic


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = 1 + request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits,
    }

    return render(request, "newspaper/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5


class TopicDetailView(generic.DetailView):
    model = Topic


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related("publishers")


class RedactorListView(generic.ListView):
    model = get_user_model()
    queryset = get_user_model().objects.all()
    paginate_by = 5


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorYearsUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorYearsUpdateForm
    template_name = "newspaper/redactor_years_update.html"
    success_url = reverse_lazy("newspaper:redactor-list")
