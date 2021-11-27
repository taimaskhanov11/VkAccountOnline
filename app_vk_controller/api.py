from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, mixins
from django.contrib.auth import models
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, User, Category, Input, Output, Message, Numbers

from .serializers import AccountSerializer, UserSerializer, MessageSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'


class MessageViewSet(viewsets.ModelViewSet): #todo убрал all
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'



    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queryset = Message.objects.all()
    #     item_name = self.request.query_params.get('give_last')
    #     if item_name:
    #             queryset =
    #
    #     return queryset


    # filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # filterset_fields = '__all__'


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-joined_at')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = '__all__'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
