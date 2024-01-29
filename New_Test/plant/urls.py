from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include("accounts.urls", namespace='accounts')),
    path('articles', include("articles.urls", namespace='articles')),
    path('', TemplateView.as_view(template_name="main/main.html") ,name="main"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
