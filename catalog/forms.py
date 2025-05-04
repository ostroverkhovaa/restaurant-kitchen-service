from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience")


class CookUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
        )
