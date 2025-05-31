from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Order, DeliveryAgent
from .forms import UserRegistrationForm, RestaurantForm, OrderForm, DeliveryAgentForm
from django.contrib.auth.models import User
import json

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'core/home.html', {'restaurants': restaurants})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            messages.success(request, 'Restaurant created successfully!')
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'core/restaurant_form.html', {'form': form})

@login_required
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'core/restaurant_detail.html', {'restaurant': restaurant})

@login_required
def place_order(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.restaurant = restaurant
            order.status = 'pending'
            
            # Calculate total amount (simplified version)
            food_items = order.food_items.split('\n')
            total = len(food_items) * 10.00  # Simplified: each item costs $10
            order.total_amount = total
            
            order.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'core/place_order.html', {'form': form, 'restaurant': restaurant})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.user != order.customer and request.user != order.restaurant.owner:
        messages.error(request, 'You do not have permission to view this order.')
        return redirect('home')
    return render(request, 'core/order_detail.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'core/my_orders.html', {'orders': orders})

@login_required
def restaurant_orders(request):
    if not request.user.restaurants.exists():
        messages.error(request, 'You do not own any restaurants.')
        return redirect('home')
    orders = Order.objects.filter(restaurant__owner=request.user).order_by('-created_at')
    return render(request, 'core/restaurant_orders.html', {'orders': orders})
