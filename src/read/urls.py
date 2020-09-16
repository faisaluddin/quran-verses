from django.urls import path
from django.views.generic import TemplateView
from .views import HomePage, subscribe ,send_feedback


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('subscribe/', subscribe, name='subscribe'),
    path('sendfeedback/',send_feedback,name='send_feedback'),
    path('contribute/', TemplateView.as_view(template_name="read/contribute.html"),name='contribute'),
    path('feedback/', TemplateView.as_view(template_name="read/feedback.html"),name='feedback'),
]
