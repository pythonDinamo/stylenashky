import requests
import warnings

from rest_framework.decorators import api_view
from main.models import Product, URL, Address
from rest_framework.response import Response

from main.serializers import ProductSerializer, ProductFilterSerializer, ProductAllSerializer

from django.shortcuts import render, redirect


from .forms import PhoneForm
from .models import Customer

# Setting to show warnings everytime when occur, as it showing only once by default.
warnings.simplefilter('always', UserWarning)


# TODO: Добавить токен телеграм-бота и chat_id пользователя, которому будут приходить сообщения (можно
#  узнать у @userinfobot).
#  Пользователь, которому будут приходить сообщения должен добавить себе @nyashki_test_bot бота.
# Telegram bot GLOBAL SETTINGS
tele_bot_token = '5032118132:AAExXf9rnoBagjg4w7ga-iwLBioNi2puRd4'  # string
chat_id = 1234567  # int



def main_view(request):
    contacts = Address.objects.all()
    phone_form = PhoneForm()
    context = {'phone_form': phone_form,
               'contacts': contacts}
    return render(request, 'index.html', context)


def phone_form_view(request):
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'complete': False}
            phone_number = phone_form.cleaned_data['user_tel']
            Customer.objects.update_or_create(user_tel=phone_number, defaults=updated_values)
            response = requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'*Поступила новая заявка:*\n\n{phone_number}',
                      'parse_mode': 'markdown'}
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


@api_view(['GET'])
def all_video(request):
    video = Product.objects.all()
    serializer = ProductSerializer(video, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_product(request, id):
    product = Product.objects.filter(id=id)
    serializer = ProductFilterSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_all(request):
    product = Product.objects.filter(published_at=True)
    serializer = ProductAllSerializer(product, many=True)
    return Response(serializer.data)
