from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import DishType, Dish, Cook


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="fish")
        self.assertEqual(
            str(dish_type),
            dish_type.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test1",
            password="test12test",
            first_name="test1",
            last_name="test1",
            years_of_experience=2
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="fish")
        dish = Dish.objects.create(
            name="salmon",
            description="baked salmon",
            price=2,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish),
                         f"{dish.name} (price: {dish.price})"
                         )

    def test_cook_get_absolute_url(self):
        cook = get_user_model().objects.create_user(
            username="test1",
            password="test12test",
            years_of_experience=2,
        )
        self.assertEqual(
            cook.get_absolute_url(),
            reverse("catalog:cook-detail", args=[str(cook.id)])
        )

    def test_dish_get_absolute_url(self):
        dish_type = DishType.objects.create(name="fish")
        dish = Dish.objects.create(
            name="salmon",
            description="baked salmon",
            price=2,
            dish_type=dish_type,
        )
        self.assertEqual(
            dish.get_absolute_url(),
            reverse("catalog:dish-detail", args=[str(dish.id)])
        )
