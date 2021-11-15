from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):

    def get(self, request, *args):
        return render(request, 'vk_accounts/index.html', {'dashboard_active':'active',
                                                          'dashboard_show':'show'})
        # return render(request, 'vk_accounts/index.html')


class ButtonsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/buttons.html', {'ui_elements_active':'active',
                                                                        'ui_elements_show':'show'})
        # return render(request, 'vk_accounts/index.html')


class DropdownsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/dropdowns.html', {'ui_elements_active':'active',
                                                                          'ui_elements_show':'show'})
        # return render(request, 'vk_accounts/index.html')


class TypographyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/ui-features/typography.html', {'ui_elements_active':'active',
                                                                           'ui_elements_show':'show'})
        # return render(request, 'vk_accounts/index.html')


class BasicElementsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/forms/basic_elements.html', {'form_element_active':'active',
                                                                         'form_element_show':'show'})
        # return render(request, 'vk_accounts/index.html')


class ChartJsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/charts/chartjs.html', {'charts_active':'active',
                                                                   'charts_show':'show'})


class BasicTableView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/tables/basic-table.html', {'tables_active':'active',
                                                                       'tables_show':'show'})


class Mdi(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/icons/mdi.html', {'icons_active':'active',
                                                              'icons_show':'show'})


class Error404View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/samples/error-404.html')


class Error500View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/samples/error-500.html')


class DocumentationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vk_accounts/documentation/documentation.html')
