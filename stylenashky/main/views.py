
import requests
import warnings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from main.models import Product, URL
from main.serializers import ProductSerializer, ProductFilterSerializer
from .forms import PhoneForm


# Setting to show warnings everytime when occur, as it showing only once by default.
warnings.simplefilter('always', UserWarning)


def main_view(request):
    phone_form = PhoneForm()
    context = {'phone_form': phone_form}
    return render(request, 'index.html', context)


def phone_form_view(request):
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            phone_form.save()
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

@api_view(['GET'])
def all_video(request):
    video = Product.objects.all()
    serializer = ProductSerializer(video, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_product(request, title):
    product = Product.objects.filter(title=title)
    serializer = ProductFilterSerializer(product, many=True)
    return Response(serializer.data)
  