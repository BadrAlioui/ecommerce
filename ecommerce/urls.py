
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_page, name='contact'),
    path('', include ('products.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
