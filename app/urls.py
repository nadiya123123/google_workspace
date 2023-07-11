from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('customers/', views.customer_list, name='customer_list'),
]