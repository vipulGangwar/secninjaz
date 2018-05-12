from django.urls import path, include, re_path
from . import views
from .views import *

urlpatterns = [
    path('test_form/',views.test_form_collection, name='collection'),
    #re_path(r'^get_details/(?P<email>.+)/$',UserList.as_view(), name='details'),
    path('get_details/',views.test_user, name='user_details')
]
