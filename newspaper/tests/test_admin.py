from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.redactor = None

    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin1",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="lolkekchebur",
            password="lolkek123",
            years_of_experience="5"
        )

    def test_redactor_years_listed(self):
        """Test redactor's years of exp is in list_display on redactor admin page"""
        url = reverse("admin:newspaper_redactor_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_detailed_years_listed(self):
        """Test redactor's years of exp is on redactor detail admin page"""
        url = reverse("admin:newspaper_redactor_change", args=[self.redactor.id])
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)
