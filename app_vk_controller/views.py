import asyncio
import time
from pprint import pprint
from threading import Thread

from django.core import serializers
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

# from app_vk_controller.db_peewee import Account
# from app_vk_controller.forms import AcceptCodeForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from app_vk_controller.models import Account, Message



class HomeView(View):

    def get(self, request, *args):
        return render(request, 'vk_accounts/index.html', {'dashboard_active': 'active',
                                                          'dashboard_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class ButtonsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/buttons.html', {'ui_elements_active': 'active',
                                                                        'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class DropdownsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/dropdowns.html', {'ui_elements_active': 'active',
                                                                          'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class TypographyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/typography.html', {'ui_elements_active': 'active',
                                                                           'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class BasicElementsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/forms/basic_elements.html', {'form_element_active': 'active',
                                                                         'form_element_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class ChartJsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/charts/chartjs.html', {'charts_active': 'active',
                                                                   'charts_show': 'show'})


class BasicTableView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/tables/basic-table.html', {'tables_active': 'active',
                                                                       'tables_show': 'show'})


class Mdi(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/icons/mdi.html', {'icons_active': 'active',
                                                              'icons_show': 'show'})


class Error404View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/samples/error-404.html')


class Error500View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/samples/error-500.html')


class DocumentationView(TemplateView):
    template_name = 'vk_accounts/documentation/documentation.html'
    # def get(self, request, *args, **kwargs):
    #     return render(request, '')


class VkAccLastMessageView(TemplateView):
    template_name = 'vk_accounts/last_messages.html'
    extra_context = {'vk_accounts_active': 'active',
                     'vk_accounts_show': 'show'}

    def get_context_data(self, **kwargs):
        context = super(VkAccLastMessageView, self).get_context_data(**kwargs)

        # data = Account.get_data()
        # context['data'] = data
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        # return HttpResponse(request.GET, request.POST)
        return {'1': 2}


class VkAccMyAccView(TemplateView):  # todo
    template_name = 'vk_accounts/my_accs.html'
    extra_context = {'vk_accounts_active': 'active',
                     'vk_accounts_show': 'show', }


def get_custom_data(request):
    if request.method == 'GET':
        data_format = request.GET.get('format')
        data_type = request.GET.get('data')
        if data_type == 'last_messages':
            # Thread(target=)
            # html = asyncio.run(init())
            # time.sleep(0.1)
            print(request.GET)
            # data = serializers.serialize('json', Account.objects.all())
            message = Message.objects.all()[:10]
            data = serializers.serialize('json', Message.objects.all().select_related('user'))
            # print(Account.objects.create(token='asdasd',name = 'ali', user_id=12312312))
            # html = Account.get_main_data()
            # data = Account.objects.all()
            pprint(data)
            return HttpResponse(data)
        else:
            return HttpResponseNotFound()
        # return JsonResponse({'1': 2})
