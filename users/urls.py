'''
Created on 2018. 10. 23.

@author: asulikeit
'''
from django.conf.urls import url
from users import views

app_name='users'

urlpatterns = [
    url(r'^$', views.UserAPIView.as_view()),
    url(r'^login/?$', views.login_by_basic, name='login by username and password'),
    url(r'^logout/?$', views.logout_by_token, name='logout by token'),
    url(r'^me/?$', views.get_myinfo, name='get my information'),
]
