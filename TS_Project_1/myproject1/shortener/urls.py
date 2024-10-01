from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('urls/', views.url_list, name='url_list'),
]