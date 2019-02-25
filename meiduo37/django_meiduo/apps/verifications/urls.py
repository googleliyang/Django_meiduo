from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^imagecodes/(?P<img_code_id>.+)/$', views.SmsImgCodeApiView.as_view(), name='imagecode'),
    url(r'^smscodes/(?P<mobile>1[345789]\d{9})/$', views.RegisterSmsApiView.as_view()),
]