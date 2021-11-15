from django.urls import path
from django.views.generic import TemplateView

from app_vk_controller import views
# app_name = 'app_vk_controller'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
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

    path('js/data.txt', TemplateView.as_view(template_name="data.txt", content_type="text/plain")),
]
