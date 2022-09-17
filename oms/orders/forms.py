from django import forms
from .models import Order, Item, Comment


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


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
        'order', 'name', 'material', 'thickness', 'color', 'dimensions', 'width', 'height', 'depth', 'fastening',
        'hole', 'rounding', 'mark', 'quantity', 'description', 'actions')

        widgets = {
            'order': forms.Select(attrs={'class': 'custom-selector'}),
            'name': forms.Select(attrs={'class': 'custom-selector'}),
            'material': forms.Select(attrs={'class': 'custom-selector'}),
            'thickness': forms.Select(attrs={'class': 'custom-selector'}),
            'color': forms.Select(attrs={'class': 'custom-selector'}),
            'dimensions': forms.Select(attrs={'class': 'custom-selector'}),
            'width': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'height': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'depth': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'fastening': forms.Select(attrs={'class': 'custom-selector'}),
            'hole': forms.TextInput(attrs={'class': 'custom-selector'}),
            'rounding': forms.TextInput(attrs={'class': 'custom-selector'}),
            'mark': forms.Select(attrs={'class': 'custom-selector'}),
            'quantity': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'description': forms.Textarea(attrs={'class': 'custom-selector'}),
            'actions': forms.SelectMultiple(attrs={'class': 'custom-selector'}),
        }


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('order', 'message')

        widgets = {
            'order': forms.Select(attrs={'class': 'custom-selector'}),
            'message': forms.Textarea(attrs={'class': 'custom-selector'}),
        }