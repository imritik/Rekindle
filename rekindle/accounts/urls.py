from django.conf.urls import url,include

from . import views


urlpatterns = [
    url(r'^$', views.SignUp.as_view(), name='signup'),
]