from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import ProfileView, ProfileListView, UserDetailView
from . import views

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile_view'),
    url(r'^profile/profile$', ProfileView.as_view(), name='profile_view'),
    url(r'^profile/update/$', views.update_profile, name='update'),
    url(r'^profile/list$', ProfileListView.as_view(), name='list'),
    url(r'^@(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='profile-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))