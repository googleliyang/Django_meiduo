from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.RegisterUsernameApiView.as_view()),
    url(r'^$', views.RegisterCreateView.as_view()),
]