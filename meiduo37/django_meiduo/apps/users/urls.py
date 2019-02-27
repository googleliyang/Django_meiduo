from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.RegisterUsernameApiView.as_view()),
    url(r'^auths/$', obtain_jwt_token),
    url(r'^emails/$', views.EmailApiView.as_view()),
    url(r'^infos/$', views.UserInfoApiView.as_view()),
    url(r'^emails/verification/$', views.EmailApiView.as_view()),
    url(r'^$', views.RegisterCreateView.as_view()),
]