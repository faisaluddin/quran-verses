from django.urls import path
from django.views.generic import TemplateView
from .views import HomePage, subscribe

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('subscribe/', subscribe, name='subscribe'),
]
