from django.conf.urls import url
from .views import QQAuthURLView, QQAuthUserView

urlpatterns = [
    url(r'^qq/statues/$', QQAuthURLView.as_view()),
    url(r'^qq/users/$', QQAuthUserView.as_view()),
]