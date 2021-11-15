from django.urls import path

from app_vk_controller import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('buttons/', views.ButtonsView.as_view(), name='buttons'),
    path('dropdowns/', views.DropdownsView.as_view(), name='dropdowns'),
    path('typography/', views.TypographyView.as_view(), name='typography'),
    path('basic_elements/', views.BasicElementsView.as_view(), name='basic_elements'),
]
