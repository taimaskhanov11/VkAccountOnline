from pyexpat import model

from django import forms

from app_answer.models import Input


class InputForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = '__all__'
