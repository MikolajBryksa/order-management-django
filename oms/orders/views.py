from django.shortcuts import render
from django.views import View
from .models import Order
from .forms import OrderAddForm
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('date')
        context = {"orders": orders}
        return render(request, 'orders/order_list.html', context)


class OrderAdd(CreateView):
    model = Order
    form_class = OrderAddForm
    template_name = 'orders/order_add.html'
    success_url = reverse_lazy('order_list')


class OrderDetails(View):
    def get(self, request, order_pk):
        order = Order.objects.get(pk=order_pk)
        context = {"order": order}
        return render(request, 'orders/order_details.html', context)


class OrderEdit(UpdateView):
    model = Order
    form_class = OrderAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('order_list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
