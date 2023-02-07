from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from rest_framework import generics, status, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Menu
from .serializers import MenuSerializer, UserSerializer


def index(request):
    menu_items = Menu.objects.all()
    return render(request, 'index.html', {'menu_items': menu_items})


class MenuAPIView(APIView):
    def get(self, request):
        m = Menu.objects.all()
        return Response({'items': MenuSerializer(m, many=True).data})


class MenuAddItemAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_new = Menu.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            price=request.data['price'],
            photo=request.data['photo'],
            # id=request.data['id']
            # id=serializers.Auto(read_only=True)

        )

        return Response({'item': MenuSerializer(item_new).data})


class RetrieveItemAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'


class DeleteItemAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]


class MenuItemUpdateAPIView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'update successful'})

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save(instance=instance)


"""
Authentication doesn't work correctly, until bugs are fixed data are accessible for every user   


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            messages.add_message(request, messages.SUCCESS, 'Login successful!')
            print("token :", token.key)
            # return Response({"token": token.key})
            return redirect('index')
        else:
            return Response({"error": "Invalid username/password"})

class LogoutView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    logout_url = 'logout/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
"""