from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/index.html')
        # return render(request, 'vk_accounts/index.html')

class ButtonsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/buttons.html')
        # return render(request, 'vk_accounts/index.html')

class DropdownsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/dropdowns.html')
        # return render(request, 'vk_accounts/index.html')

class TypographyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/typography.html')
        # return render(request, 'vk_accounts/index.html')

class BasicElementsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/forms/basic_elements.html')
        # return render(request, 'vk_accounts/index.html')
