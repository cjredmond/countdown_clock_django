from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from countdown.views import IndexView, ImageCreateView, CountdownCreateView,\
                            CountdownView, PassThroughView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^pass/$', PassThroughView.as_view(), name='pass_through_view'),
    url(r'^add_image/(?P<pk>.+/)$', ImageCreateView.as_view(), name='image_create_view'),
    url(r'^new_countdown/$', CountdownCreateView.as_view(), name='countdown_create_view'),
    url(r'^countdown/(?P<pk>.+)/$', CountdownView.as_view(), name='countdown_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
