from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from countdown.views import IndexView, ImageCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^add_image/$', ImageCreateView.as_view(), name='image_create_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
