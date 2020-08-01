from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='idpdatacollection-home'),
    path('about/', views.about, name='idpdatacollection-about')
]