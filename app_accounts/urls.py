from django.urls import path, include

from app_accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', views.RegisterView.as_view(), name='register'),
    # path('accounts/profile/', ProfileView.as_view(), name='profile')
]