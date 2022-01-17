import requests
from rest_framework.decorators import api_view
from main.models import Product, URL
from rest_framework.response import Response

from main.serializers import ProductSerializer, ProductFilterSerializer, ProductAllSerializer
import warnings

from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PhoneForm


# Setting to show warnings everytime when occur, as it showing only once by default.
from .models import Customer

warnings.simplefilter('always', UserWarning)


def main_view(request):
    phone_form = PhoneForm()
    context = {'phone_form': phone_form}
    return render(request, 'index.html', context)


def phone_form_view(request):
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'complete': False}
            phone_number = phone_form.cleaned_data['user_tel']
            Customer.objects.update_or_create(user_tel=phone_number, defaults=updated_values)
            # TODO: Добавить токен телеграм-бота и chat_id пользователя, которому будут приходить сообщения (можно
            #  узнать у @userinfobot)
            tele_bot_token = ''  # string
            chat_id = 123456  # int
            response = requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id, 'text': f'{request.POST["user_tel"]}'}
            ).json()
            if not response.get('ok', False):
                warnings.warn(f'''
                ВНИМАНИЕ!!!
                Не удалось отправить сообщение телеграм боту или формат ответа изменился.
                Код ошибки: {response.get("error_code", "Не удалось получить код ошибки.")} 
                Описание ошибки: {response.get("description", "Не удалось получить описание ошибки.")}''')
            return redirect('main_view')
    context = {'phone_form': phone_form}
    return render(request, 'index.html', context)
