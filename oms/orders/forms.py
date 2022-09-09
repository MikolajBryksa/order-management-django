from django import forms
from .models import Order


class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('seller', 'customer', 'designer', 'status')

        widgets = {
            'seller': forms.Select(attrs={'class': 'custom-selector'}),
            'customer': forms.TextInput(attrs={'class': 'custom-selector'}),
            'designer': forms.Select(attrs={'class': 'custom-selector'}),
            'status': forms.Select(attrs={'class': 'custom-selector'}),
        }
