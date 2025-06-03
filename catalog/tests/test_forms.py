from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.forms import CookCreationForm
from catalog.models import DishType, Dish, Cook


class SearchFormTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(
            name="fish",
        )
        self.dish = Dish.objects.create(
            name="salmon",
            description="baked salmon",
            price=2,
            dish_type=self.dish_type,
        )
        self.cook = Cook.objects.create_user(
            username="test1",
            password="test12test",
            years_of_experience=2,
        )

    def test_cook_search(self):
        response = self.client.get(
            reverse("catalog:cook-list") + "?username=test"
        )
        self.assertContains(response, "test")

    def test_dish_search(self):
        response = self.client.get(reverse("catalog:dish-list") + "?name=salmon")
        self.assertContains(response, "salmon")


class FormsTest(TestCase):
    def test_form_is_valid(self):
        form_data = {
            "username": "test",
            "years_of_experience": 2,
            "first_name": "test",
            "last_name": "test",
            "password1": "user12test",
            "password2": "user12test",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

        cleaned = form.cleaned_data
        self.assertEqual(cleaned["username"], form_data["username"])
        self.assertEqual(cleaned["years_of_experience"], form_data["years_of_experience"])
        self.assertEqual(cleaned["first_name"], form_data["first_name"])
        self.assertEqual(cleaned["last_name"], form_data["last_name"])

    def test_invalid_years_of_experience(self):
        form_data = {
            "username": "test",
            "years_of_experience": -2,
            "first_name": "test",
            "last_name": "test",
            "password1": "user12test",
            "password2": "user12test",
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)
