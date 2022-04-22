from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from meusite.views import view_404
handler404 = view_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meusite.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
