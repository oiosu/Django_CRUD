import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user, register
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path("register", register, name="register"),
    path("get_user/<int:user_id>", get_user),
]
