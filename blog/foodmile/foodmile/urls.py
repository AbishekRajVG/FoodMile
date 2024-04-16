from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodmileblog.urls')),
    # path('*/password', include('foodmileusers.urls')),
    path('user/', include('django.contrib.auth.urls')),  # django auth package will take care of login logout reg urls
    path('user/', include('foodmileusers.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)