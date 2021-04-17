from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserList.as_view())

urlpatterns =[
    url(r'^home', views.UserList.as_view()),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^event', views.EventList.as_view()),
    url(r'^editevent/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^category', views.CategoryList.as_view()),
    url(r'^editcategory/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^showeventoncategory/(?P<pk>[0-9]+)/$', views.ShowEventOnCategoryDetails.as_view()),
    url(r'^TopEventOnCategoryDetails', views.TopEventOnCategoryDetails.as_view()),

    ]

