from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('^infos', views.AreaModelViewSet, base_name='area')
router.register('^address', views.AddressModelViewSet, base_name='address')
# router.register('shi', views.ShiApiView, base_name='')
urlpatterns = [
    url('^area/(?P<pk>\d*)$', views.AreaApiView.as_view())
]
urlpatterns += router.urls
