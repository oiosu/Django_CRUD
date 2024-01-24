from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             "nickname",
#             "profile_pic",
#             "introduce",
#         ]
#         widget = {
#             "introduce": forms.Textarea,
#         }