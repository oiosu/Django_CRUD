from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from articles import views

# from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path("home", include("pages.urls")),
    path("articles/", include("articles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
