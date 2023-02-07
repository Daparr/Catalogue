import io
from abc import ABC

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from .models import Menu


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class MenuModel:
    def __init__(self, title, description, price, id):
        self.title = title
        self.description = description
        self.price = price
        self.id = id


class MenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    photo = serializers.FileField()
    price = serializers.IntegerField(min_value=0)

    class Meta:
        model = Menu
        fields = ('id', 'title', 'description', 'price', 'photo')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.photo = validated_data.get('photo', instance.photo)
        # instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance


"""

Test leftovers

def encode():
    model = MenuModel("Лазанья", "Склад лазаньї", "90", "3")
    model_sr = MenuSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title": "TEST TITLE", "description": "TEST DESCRIPTION", "price": 1, "id": 4}')
    data = JSONParser().parse(stream)
    serializer = MenuSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
"""
