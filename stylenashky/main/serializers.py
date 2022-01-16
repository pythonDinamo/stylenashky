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
        fields = ["title", "massa", "avg_price"]