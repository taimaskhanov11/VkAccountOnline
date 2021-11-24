from django import forms


class AcceptCodeForm(forms.Form):
    code = forms.CharField(required=True, max_length=10, label='Код подтверждения')
