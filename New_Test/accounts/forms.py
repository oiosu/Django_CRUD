from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import UserProfile
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        
    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if not profile_picture:
            # 기본 이미지 경로로 설정
            profile_picture = 'path/to/default/image.jpg'
        return profile_picture