from django.urls import path

from .views import (
    index,
    DishTypeListView,
    CookListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "catalog"