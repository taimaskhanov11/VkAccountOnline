from django.urls import path

from app_answer.views import AnswerListView

urlpatterns = [
    path('answer/', AnswerListView.as_view(), name='answer'),
]
