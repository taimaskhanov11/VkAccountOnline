from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from app_vk_controller import views
from app_vk_controller.api import AccountViewSet, UserViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)
router.register('users', UserViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),

    path('vk-accs/', views.VkAccountListView.as_view(), name='vk_accs'),
    path('vk-accs/<pk>/', views.VkAccountDetailView.as_view(), name='vk_acc_detail'),
    path('vk-users/', views.VkUserListView.as_view(), name='vk_users'),
    path('vk-users/<pk>/', views.VkUserDetailView.as_view(), name='vk_user_detail'),

    path('messages/', views.MessageListView.as_view(), name='messages'),
    path('messages/<pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('messages/vk-users/<pk>/', views.MessageByUserListView.as_view(), name='messages_by_user'),
    path('messages/vk-accs/<pk>/', views.MessagesByAccountListView.as_view(), name='messages_by_account'),
    path('last-messages/', views.LastMessageListView.as_view(), name='last_messages'),

    path('numbers/', views.NumberListView.as_view(), name='numbers'),
    path('numbers/<pk>/', views.NumberDetailView.as_view(), name='number_detail'),
    path('numbers/vk-accs/<pk>/', views.NumberByAccountListView.as_view(), name='numbers_by_account'),



    path('buttons/', views.ButtonsView.as_view(), name='buttons'),
    path('dropdowns/', views.DropdownsView.as_view(), name='dropdowns'),
    path('typography/', views.TypographyView.as_view(), name='typography'),
    path('basic-elements/', views.BasicElementsView.as_view(), name='basic_elements'),
    path('chartjs/', views.ChartJsView.as_view(), name='chartjs'),
    path('basic-table/', views.BasicTableView.as_view(), name='basic_table'),
    path('basic-elements/', views.BasicElementsView.as_view(), name='basic_elements'),
    path('mdi/', views.Mdi.as_view(), name='mdi'),

    path('error-404/', views.Error404View.as_view(), name='error_404'),
    path('error-500/', views.Error500View.as_view(), name='error_500'),
    path('documentation/', views.DocumentationView.as_view(), name='documentation'),


    path('js/data.txt', TemplateView.as_view(template_name="data.txt", content_type="text/plain")), #todo
    path('messages/js/data.txt', TemplateView.as_view(template_name="data.txt", content_type="text/plain")),

    path('vk-accounts/data/', views.get_custom_data, name='custom_data')  # todo убрать начало
]
