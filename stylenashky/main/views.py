from django.shortcuts import render
from rest_framework.decorators import api_view
from main.models import Product, URL
from rest_framework.response import Response

from main.serializers import ProductSerializer, ProductFilterSerializer, ProductAllSerializer


def main_view(request):
    return render(request, 'index.html')


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


@api_view(['GET'])
def product_all(request):
    product = Product.objects.filter(published_at=True)
    serializer = ProductAllSerializer(product, many=True)
    return Response(serializer.data)
