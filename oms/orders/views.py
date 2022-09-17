from django.shortcuts import render
from django.views import View
from .models import Order, Item, Comment
from .forms import OrderAddForm, ItemAddForm, CommentAddForm
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('date')
        context = {"orders": orders}
        return render(request, 'orders/order_list.html', context)


class Menu(View):
    def get(self, request):
        return render(request, 'orders/menu.html')


class OrderDetails(View):
    def get(self, request, order_pk):
        order = Order.objects.get(pk=order_pk)
        comments = Comment.objects.filter(order=order_pk).order_by('date')
        items = Item.objects.filter(order=order_pk).order_by('pk')
        context = {"order": order, "items": items, "comments": comments}
        return render(request, 'orders/order_details.html', context)


class OrderAdd(CreateView):
    model = Order
    form_class = OrderAddForm
    template_name = 'orders/order_add.html'
    success_url = reverse_lazy('order_list')


class OrderEdit(UpdateView):
    model = Order
    form_class = OrderAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')


class ItemAdd(CreateView):
    model = Item
    form_class = ItemAddForm
    template_name = 'orders/item_add.html'
    success_url = reverse_lazy('order_list')


class ItemEdit(UpdateView):
    model = Item
    form_class = ItemAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('order_list')


class CommentAdd(CreateView):
    model = Comment
    form_class = CommentAddForm
    template_name = 'orders/comment_add.html'
    success_url = reverse_lazy('order_list')


class CommentEdit(UpdateView):
    model = Comment
    form_class = CommentAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('order_list')
