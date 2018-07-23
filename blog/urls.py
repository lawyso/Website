from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views
app_name='blog'
urlpatterns = [
    url(r'^home/$',views.BlogList.as_view(),name='blog'),


    url(r'^(?P<pk>\d+)$',views.blog_details,name='details'),

]