from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import user,homepage,login_page,about

urlpatterns = [
	url(r'^$',homepage),
	url(r'^about/$',about),
	url(r'^login/$',login_page),
    url(r'^user/$',user),

    ]