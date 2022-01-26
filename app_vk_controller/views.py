from pprint import pprint

from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView

# from app_vk_controller.db_peewee import Account
# from app_vk_controller.forms import AcceptCodeForm
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_vk_controller.forms import UserForm, MessageForm
from app_vk_controller.models import Account, Message, User, Number, SendMessage
from app_vk_controller.service import VkAccountDataMixin, MessageColumnEnum


class HomeView(View):

    def get(self, request, *args):
        return render(request, 'app_vk_controller/index.html', {'dashboard_active': 'active',
                                                                'dashboard_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class ButtonsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/ui-features/buttons.html', {'ui_elements_active': 'active',
                                                                              'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class DropdownsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/ui-features/dropdowns.html', {'ui_elements_active': 'active',
                                                                                'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class TypographyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/ui-features/typography.html', {'ui_elements_active': 'active',
                                                                                 'ui_elements_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class BasicElementsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/forms/basic_elements.html', {'form_element_active': 'active',
                                                                               'form_element_show': 'show'})
        # return render(request, 'vk_accounts/index.html')


class ChartJsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/charts/chartjs.html', {'charts_active': 'active',
                                                                         'charts_show': 'show'})


class BasicTableView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/tables/basic-table.html', {'tables_active': 'active',
                                                                             'tables_show': 'show'})


class Mdi(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/icons/mdi.html', {'icons_active': 'active',
                                                                    'icons_show': 'show'})


class Error404View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/samples/error-404.html')


class Error500View(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app_vk_controller/samples/error-500.html')


class DocumentationView(TemplateView):
    template_name = 'app_vk_controller/documentation/documentation.html'
    # def get(self, request, *args, **kwargs):
    #     return render(request, '')


class MessageDetailView(VkAccountDataMixin, DetailView):
    model = Message
    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}


class MessageCreateView(VkAccountDataMixin, CreateView):
    model = Message
    form_class = MessageForm

    # fields = ['text', 'account', 'user']

    # initial = {
    # }
    # def get(self, request, *args, **kwargs):
    #     get = super().get(request, *args, **kwargs)
    #     return get

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        SendMessage.objects.create(message=self.object)
        return response

    # def get_initial(self):
    #     user = self.request.GET.get('user')
    #     account = self.request.GET.get('account', )
    #     if account and user:
    #         print('asdsa')
    #
    #         return {
    #             'account': account,
    #             'user': user,
    #         }
    #     else:
    #         super().get_initial()


class MessageListView(VkAccountDataMixin, ListView):
    model = Message
    paginate_by = 10
    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show',
    #                  'table_fields': enum._member_names_
    #                  }
    # search = None
    queryset = Message.objects.all().select_related('account', 'user')

    def get_queryset(self):
        search_field = self.request.GET.get('search_field')
        search = self.request.GET.get('search')
        if search_field and search:
            return self.searching(search_field, search)
        else:
            return super().get_queryset()

        # res = self.search or super().get_queryset(search_field)
        # print(self.search)
        # return res

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_field = self.request.GET.get('search_field', '')
        search = self.request.GET.get('search', '')

        context['s'] = f"search_field={search_field}&search={search}&"
        context['title'] = f'Поле {self.column_enum(int(search_field)).name} поиск:' \
                           f' {search}' if search_field else 'Все сообщения'
        return context

    def searching(self, field, search):
        field = MessageColumnEnum(int(field))
        res = self.queryset
        match field:
            case self.column_enum.Account_ID:
                res = self.queryset.filter(account=search)
            case self.column_enum.User_ID:
                res = self.queryset.filter(user=search)

            case self.column_enum.Text:
                res = self.queryset.filter(text__icontains=search)
            case self.column_enum.Template:
                res = self.queryset.filter(answer_template__icontains=search)
            case self.column_enum.Answer:
                res = self.queryset.filter(answer_question__icontains=search)
            case self.column_enum.User:
                res = self.queryset.filter(user__first_name__icontains=search)
            case self.column_enum.Account:
                res = self.queryset.filter(account__first_name__icontains=search)
            case self.column_enum.Date:
                res = self.queryset.filter(sent_at__icontains=search)
        return res
        # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}

    # def get(self, request, *args, **kwargs):
    #     get = super().get(request, *args, **kwargs)
    #     print(self.request.GET, 'GET')
    #     return get

    # def post(self, request, *args, **kwargs):
    #     print(self.request.POST, 'POST')
    #     search_field = self.request.POST.get('search_field')
    #     search = self.request.POST.get('search')
    #     print(search_field)
    #     print(self.enum._value2member_map_)
    #     if int(search_field) in self.enum._value2member_map_:
    #         self.search = self.searching(search_field, search)
    #         print(self.search)
    #     # self.object_list = self.search
    #     # context = self.get_context_data()
    #
    #     # self.object_list = self.get_queryset()
    #     # allow_empty = self.get_allow_empty()
    #     # return self.get(request, *args, **kwargs)
    #     # context['s'] = f"{self.request.POST.get('search')}&{self.request.POST.get('search_field')}&"
    #     # context['s'] = f"{self.request.POST.get('search')}&"
    #     # self.get()
    #     # print(context)
    #     return self.get(request, *args, **kwargs)
    #     # return render(request, 'app_vk_controller/message_list.html', context)


class MessageByUserListView(VkAccountDataMixin, ListView):
    model = Message
    paginate_by = 10
    queryset = Message.objects.all().select_related('account', 'user')

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}
    def get_queryset(self):
        # return Message.objects.filter(user__pk=self.kwargs['pk']).all()
        return self.queryset.filter(user__pk=self.kwargs['pk']).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Сообщения Пользователя {User.objects.get(pk=self.kwargs["pk"])}'
        return context


class MessagesByAccountListView(VkAccountDataMixin, ListView):
    model = Message
    paginate_by = 10
    queryset = Message.objects.all().select_related('account', 'user')

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}
    def get_queryset(self):
        # return Message.objects.filter(account__pk=self.kwargs['pk']).all()
        return self.queryset.filter(account__pk=self.kwargs['pk']).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Сообщения Аккаунта {Account.objects.get(pk=self.kwargs["pk"])}'
        return context


class LastMessageListView(VkAccountDataMixin, TemplateView):
    """Подгрузка с помощью javascript """
    template_name = 'app_vk_controller/last_messages.html'
    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}


class VkAccountListView(VkAccountDataMixin, ListView):  # todo
    model = Account
    template_name = 'app_vk_controller/vk_accounts_list.html'

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('account')
        # print(request.POST)
        account = Account.objects.get(pk=pk)
        if account.start_status:
            account.start_status = False
        else:
            account.start_status = True
        account.save()
        return self.get(request, *args, **kwargs)


class VkAccountDetailView(VkAccountDataMixin, DetailView):
    model = Account
    template_name = 'app_vk_controller/vk_account_detail.html'
    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}


class VkUserDetailView(VkAccountDataMixin, DetailView, UpdateView):
    model = User
    template_name = 'app_vk_controller/vk_user_detail.html'
    form_class = UserForm

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = {
            'Дата присоединения': self.object.joined_at,
            'Город': self.object.city,
            'Последнее сообщение': self.object.messages.first(),
            'Ссылка в ВКонтакте': f'https://vk.com/id{self.object.user_id}',
            'Прикреплен к боту': self.object.account,
            'Текущая стадия': self.object.state,
            'Статус блокировки': self.object.blocked,

        }
        return context

    def form_valid(self, form):
        valid = super().form_valid(form)
        self.extra_context.update(status_succes='Обновлено')
        print(valid)
        return valid
    # def post(self, request, *args, **kwargs):
    #     state = request.POST.get('state')
    #     status = request.POST.get('status')
    #     self.object.state = int(state)
    #     print(self.request.POST)
    #     print(self.request.GET)
    #     return self.get(request, *args, **kwargs)


class VkUserListView(VkAccountDataMixin, ListView):
    model = User
    template_name = 'app_vk_controller/vk_users_list.html'

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('user')
        print(request.POST)
        user = User.objects.get(pk=pk)
        if user.blocked:
            user.blocked = False
        else:
            user.blocked = True
        user.save()
        return self.get(request, *args, **kwargs)


class NumberListView(VkAccountDataMixin, ListView):
    model = Number
    queryset = Number.objects.all().select_related('account', 'user')

    # template_name = 'app_vk_controller/number_detail.html'

    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}

    def get_queryset(self):
        search_field = self.request.GET.get('search_field')
        search = self.request.GET.get('search')
        if search_field and search:
            if MessageColumnEnum(int(search_field)) == self.column_enum.Account_ID:
                return self.queryset.filter(account=search)
        else:
            return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_field = self.request.GET.get('search_field', '')
        search = self.request.GET.get('search', '')

        context['s'] = f"search_field={search_field}&search={search}&"
        context['title'] = f'Поле {self.column_enum(int(search_field)).name} поиск:' \
                           f' {search}' if search_field else 'Все номера'
        return context


class NumberDetailView(VkAccountDataMixin, ListView):
    model = Number
    # template_name = 'app_vk_controller/number_list.html'
    # extra_context = {'vk_accounts_active': 'active',
    #                  'vk_accounts_show': 'show'}


class NumberByAccountListView(VkAccountDataMixin, ListView):
    model = Number
    queryset = Number.objects.all().select_related('account', 'user')

    def get_queryset(self):
        # return Number.objects.filter(account__pk=self.kwargs['pk']).all()
        return self.queryset.filter(account__pk=self.kwargs['pk']).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'All Got {Account.objects.get(pk=self.kwargs["pk"])} Numbers'
        return context


class SearchView(ListView):  # todo
    template_name = 'clothes/search.html'
    context_object_name = 'clothess'
    paginate_by = 6

    def get_queryset(self):
        print(self.request.GET)
        return Message.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Результаты по "{self.request.GET.get("s")}"'
        # print(self.queryset)
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['clothes'] = context['clothess'].first()
        return context


# old
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
