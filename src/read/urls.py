from django.urls import path
from django.views.generic import TemplateView
from .views import HomePage, SubscribeView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('subscribe', SubscribeView.as_view(), name='subscribe'),
]
