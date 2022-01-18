from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from FRS import views as frs_views
urlpatterns = [
    path('' , include('accounts.urls')),
    path('profile/', frs_views.profile, name='profile'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)