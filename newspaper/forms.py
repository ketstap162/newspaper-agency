from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspaper.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_exp(self):  # this logic is optional, but possible
        return validate_years_of_exp(self.cleaned_data["license_number"])


class RedactorYearsUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["years_of_experience"]

    def clean_license_number(self):
        return validate_years_of_exp(self.cleaned_data["years_of_experience"])


def validate_years_of_exp(years):
    if years <= 0:
        raise ValidationError("License number should consist of 8 characters")
    return years
