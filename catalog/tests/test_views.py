from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import DishType, Dish

DISH_TYPE_URL = reverse("catalog:dish-type-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="fish")
        DishType.objects.create(name="salad")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(list(response.context["dish_type_list"]), list(dish_types))
        self.assertTemplateUsed(response, "catalog/dish_type_list.html")


class ToggleCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
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

    def test_toggle_cook_add_and_remove(self):
        toggle_url = reverse("catalog:toggle-cook", args=[self.dish.pk])

        response = self.client.post(toggle_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.user, self.dish.cooks.all())

        response = self.client.post(toggle_url)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.user, self.dish.cooks.all())


class DishesByTypeViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.dish_type = DishType.objects.create(name="fish")
        self.dish_salmon = Dish.objects.create(
            name="salmon", description="saked salmon", price=2, dish_type=self.dish_type
        )
        self.dish_tuna = Dish.objects.create(
            name="tuna", description="grilled tuna", price=3, dish_type=self.dish_type
        )

    def test_view_returns_correct_context(self):
        self.client.login(
            username="test",
            password="test1234",
        )
        url = reverse("catalog:dishes-by-type", args=[self.dish_type.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["dish_type"], self.dish_type)
        self.assertIn(self.dish_salmon, response.context["dishes"])
        self.assertIn(self.dish_tuna, response.context["dishes"])
        self.assertTemplateUsed(response, "catalog/dishes_by_type.html")
