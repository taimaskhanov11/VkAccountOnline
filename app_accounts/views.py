from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')
