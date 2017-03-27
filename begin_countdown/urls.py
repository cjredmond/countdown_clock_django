from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from countdown.views import ImageCreateView, CountdownCreateView,\
                            CountdownView, PassThroughView, ImageDeleteView, \
                            ManageView, TitleView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pass/$', PassThroughView.as_view(), name='pass_through_view'),
    url(r'^manage/(?P<pk>.+)/$', ImageCreateView.as_view(), name='image_create_view'),
    url(r'^image/(?P<pk>\d+)/delete/$', ImageDeleteView.as_view(), name='image_delete_view'),
    url(r'^$', CountdownCreateView.as_view(), name='countdown_create_view'),
    url(r'^countdown/(?P<pk>.+)/$', CountdownView.as_view(), name='countdown_view'),
    url(r'^test/(?P<pk>.+)/$', ManageView.as_view(), name='manage_view'),
    url(r'^test/(?P<sk>.+)/title/(?P<pk>\d+)$', TitleView.as_view(), name='title_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
