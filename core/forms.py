from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Restaurant, DeliveryAgent

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['food_items', 'delivery_address']
        widgets = {
            'food_items': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter food items (one per line)'}),
            'delivery_address': forms.Textarea(attrs={'rows': 3}),
        }

class DeliveryAgentForm(forms.ModelForm):
    class Meta:
        model = DeliveryAgent
        fields = ['phone', 'current_location'] 