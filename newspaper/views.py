from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django_superuser_required.views import SuperuserRequiredMixin
from newspaper.forms import (
    RedactorCreationForm,
    RedactorYearsUpdateForm,
    RedactorFullUpdateForm,
    NewspaperForm,
    SearchForm,
)
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
    queryset = Topic.objects.all()
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["search_form"] = SearchForm(
            initial={"search_by": self.request.GET.get("search_by", "")}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)

        if form.is_valid():
            result = self.queryset.filter(
                name__icontains=form.cleaned_data["search_by"]
            )
            return result
        return self.queryset


class TopicDetailView(generic.DetailView):
    model = Topic
    queryset = Topic.objects.prefetch_related("newspapers")


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["search_form"] = SearchForm(
            initial={"search_by": self.request.GET.get("search_by", "")}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)

        if form.is_valid():
            result = self.queryset.filter(
                title__icontains=form.cleaned_data["search_by"]
            )
            return result
        return self.queryset


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related("publishers").select_related(
        "topic"
    )


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(generic.ListView):
    model = get_user_model()
    queryset = get_user_model().objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["search_form"] = SearchForm(
            initial={"search_by": self.request.GET.get("search_by", "")}
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)

        if form.is_valid():
            result = self.queryset.filter(
                username__icontains=form.cleaned_data["search_by"]
            )
            return result
        return self.queryset


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorYearsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorYearsUpdateForm
    template_name = "newspaper/redactor_form.html"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorFullUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorFullUpdateForm
    template_name = "newspaper/redactor_form.html"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
