from django.shortcuts import render
from django.views import View
from .models import Order, Item, Comment
from .forms import OrderAddForm, ItemAddForm, CommentAddForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


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


class OrderAdd(PermissionRequiredMixin, CreateView):
    permission_required = 'orders.add_order'
    model = Order
    form_class = OrderAddForm
    template_name = 'orders/order_add.html'
    success_url = reverse_lazy('order_list')


class OrderDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'orders.delete_order'
    model = Order
    success_url = reverse_lazy('order_list')


class OrderEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Order
    form_class = OrderAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class ItemAdd(PermissionRequiredMixin, CreateView):
    permission_required = 'orders.add_item'
    model = Item
    form_class = ItemAddForm
    template_name = 'orders/item_add.html'
    success_url = reverse_lazy('order_list')


class ItemDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'orders.delete_item'
    model = Item
    success_url = reverse_lazy('order_list')


class ItemEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'orders.change_item'
    model = Item
    form_class = ItemAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class CommentAdd(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Comment
    form_class = CommentAddForm
    template_name = 'orders/comment_add.html'
    success_url = reverse_lazy('order_list')


class CommentDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Comment
    success_url = reverse_lazy('order_list')


class CommentEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Comment
    form_class = CommentAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')
