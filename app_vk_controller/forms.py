from django import forms

from app_vk_controller.models import User, Message, Account


class AcceptCodeForm(forms.Form):
    code = forms.CharField(required=True, max_length=10, label='Код подтверждения')


class UserForm(forms.ModelForm):
    # blocked = forms.CheckboxInput(attrs={'class': 'form-control'}),
    state = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    blocked = forms.BooleanField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'status-input',
               }
    ))

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['blocked', 'state']
        # widgets = {'input': forms.HiddenInput()}


class MessageForm(forms.ModelForm):
    # account = forms.CharField(widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    account = forms.ModelChoiceField(label='От кого',queryset=Account.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    user = forms.ModelChoiceField(label='Кому',queryset=User.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    # user = forms.CharField(widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    answer_question = forms.CharField(label='Текст',widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Message
        fields = ['account', 'user', 'answer_question']
