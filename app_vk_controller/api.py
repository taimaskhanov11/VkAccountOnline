from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, mixins
from django.contrib.auth import models
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, User, Category, Input, Output, Message, Number

from .serializers import AccountSerializer, UserSerializer, MessageSerializer, NumberSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'




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



class MessageViewSet(viewsets.ModelViewSet):  # todo убрал all
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    # search_fields = '__all__'
    search_fields = ["answer_question", "answer_template", "id", "sent_at", "text", ]
    ordering_fields = '__all__'

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class CustomSearchFilter(filters.SearchFilter):  # OLD #todo
    def get_search_fields(self, view, request):
        print(request.query_params)
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)




