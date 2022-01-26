from django.urls import path, include
from rest_framework import routers

from app_answer.api import CategoryViewSet, InputViewSet, OutputViewSet
from app_answer.views import AnswerListView


urlpatterns = [

    path('answer/', AnswerListView.as_view(), name='answer'),

]
