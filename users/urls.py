'''
Created on 2018. 10. 23.

@author: asulikeit
'''
from django.conf.urls import url
from users import views

app_name='users'

urlpatterns = [
    url(r'^$', views.UserAPIView.as_view()),
    url(r'^login/?$', views.login, name='login by username and password'),
    url(r'^me/?$', views.get_myinfo, name='get my information'),
]
