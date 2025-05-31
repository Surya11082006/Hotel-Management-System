from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Restaurant URLs
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/orders/', views.restaurant_orders, name='restaurant_orders'),
    
    # Order URLs
    path('order/<int:restaurant_id>/place/', views.place_order, name='place_order'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/my/', views.my_orders, name='my_orders'),
] 