from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

admin.site.site_title = "Admin panel"
admin.site.site_header = "Admin panel"
admin.site.index_title = "Admin panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.post_list, name='post_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)