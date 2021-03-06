
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('saints.urls')),
    path('auth/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('media/', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
