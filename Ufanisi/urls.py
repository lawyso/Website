from django.conf.urls import url
from Ufanisi import views
app_name= 'Ufanisi'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view(),name='about'),
    url(r'^projects/$', views.MissionPageView.as_view(),name='projects'),
    url(r'^blog/$', views.BlogPageView.as_view(),name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'portal/', views.MembersArea.as_view(), name='members-home'),
]