from django.conf.urls import url
from booking import views
urlpatterns = [
    url('^$', views.booking,name='booking'),
   ]