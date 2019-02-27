from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()

# router.register('', views.AreaViewSet, base_name='')
# router.register('shi', views.ShiApiView, base_name='')
urlpatterns = [
    url('^area/(?P<pk>\d*)$', views.AreaApiView.as_view())
]
# urlpatterns += router.urls
