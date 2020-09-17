from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django import template
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from utils.email import send_email

from utils.email_templates import single_verse_template as svt

from .tasks import registration_email
from .models import Subscriber
from .forms import SubscriberForm
from .constants import feedback_email
from .tasks import send_single_ayah


class HomePage(TemplateView):
    template_name = "read/homepage.html"
    send_single_ayah()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = "home"
        return context


@require_http_methods(['POST'])
def subscribe(request, *args, **kwargs):
    user = SubscriberForm(request.POST)
    if user.is_valid():
        user.save()
        return JsonResponse({'message': 'Success'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid Data'}, status=400)


@require_http_methods(['POST'])
def send_feedback(request, *args, **kwargs):
    body = f"First name:{request.POST.get('firstname')} Email:{request.POST.get('mailid')} Message:{request.POST.get('subject')}"
    send_email(feedback_email['subject'].format(
        name=request.POST.get('firstname')), feedback_email['body'].format(name=request.POST.get('firstname'),
                                                                           country=request.POST.get(
                                                                               'country'),
                                                                           message=request.POST.get('subject'), email=request.POST.get('mailid')), ["quranverses66@gmail.com"]),
    return JsonResponse({'message': 'success'})
