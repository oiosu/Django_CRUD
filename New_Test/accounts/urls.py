from django.urls import path
from . import views
from .views import view_profile, edit_profile

app_name = "accounts"

urlpatterns = [
    path("<int:pk>/follow/", views.follow, name="follow"),
    path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
