from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("<str:pk>/follow/", views.follow, name="follow"),
    # path("<str:pk>/", views.detail, name="detail"),  # <str:pk>로 수정
    path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
