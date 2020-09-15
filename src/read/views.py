from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django import template
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from utils.email_templates import single_verse_template as svt

from .tasks import registration_email
from .models import Subscriber
from .forms import SubscriberForm


class HomePage(TemplateView):
    template_name = "read/homepage.html"
    context = template.Context({'ayah': '262',
                                'arabic': 'اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ255',
                                'english': 'Allah - there is no deity except Him, the Ever-Living, the Sustainer of [all] existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is [presently] before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.'})
    # send_email('Test', svt(context=context), [
    #           'faisaluddin01@gmail.com'], content_type='html')


@require_http_methods(['POST'])
def subscribe(request, *args, **kwargs):
    user = SubscriberForm(request.POST)
    if user.is_valid():
        user.save()
        return JsonResponse({'message': 'Success'}, status=201)
    else:
        print(user.errors)
        return JsonResponse({'error': 'Invalid Data'}, status=400)
