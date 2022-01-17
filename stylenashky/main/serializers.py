from rest_framework import serializers
from .models import Product, URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["url"]


class ProductSerializer(serializers.ModelSerializer):
    url = URLSerializer(many=True)
    class Meta:
        model = Product
        fields = ["number_product", "url"]


class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["massa", "avg_price", "stock_in_bag"]


class ProductAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title"]
