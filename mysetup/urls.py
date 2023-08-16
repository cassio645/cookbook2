from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

handler404 = 'myapp.views.page_not_found'
handler500 = 'myapp.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path("usuario/", include("users.urls")),
    path("usuario/", include("django.contrib.auth.urls")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)