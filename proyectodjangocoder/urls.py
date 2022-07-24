from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from tienda.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entrada),
    path('tienda/', include('tienda.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = not_found
