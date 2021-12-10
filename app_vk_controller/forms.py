from django import forms

from app_vk_controller.models import User


class AcceptCodeForm(forms.Form):
    code = forms.CharField(required=True, max_length=10, label='Код подтверждения')


class UserForm(forms.ModelForm):
    # blocked = forms.CheckboxInput(attrs={'class': 'form-control'}),
    state = forms.IntegerField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    blocked = forms.BooleanField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'status-input',
               }
    ))

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['blocked', 'state']
        # widgets = {'input': forms.HiddenInput()}
