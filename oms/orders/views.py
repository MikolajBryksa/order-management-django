from django.shortcuts import render, redirect
from django.views import View
from .models import Order, Item, Comment
from .forms import OrderAddForm, ItemAddForm, CommentAddForm, SearchForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Count
from .filters import OrderFilter


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('date')
        context = {"orders": orders}
        return render(request, 'orders/order_list.html', context)


class Stats(View):
    def get(self, request):
        marek = Order.objects.filter(seller="Marek").count()
        natalia = Order.objects.filter(seller="Natalia").count()
        joanna = Order.objects.filter(seller="Joanna").count()
        context = {"marek": marek, "natalia": natalia, "joanna": joanna}
        return render(request, 'orders/stats.html', context)


class Info(View):
    def get(self, request):
        return render(request, 'orders/info.html')


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
    success_url = "/order_details/{order_id}"

    def get_initial(self):
        order_pk = self.kwargs["order_pk"]
        data = super().get_initial()
        data["order"] = Order.objects.get(pk=order_pk)
        return data


class ItemDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'orders.delete_item'
    model = Item
    success_url = "/order_details/{order_id}"


class ItemEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'orders.change_item'
    model = Item
    form_class = ItemAddForm
    template_name_suffix = '_edit'
    success_url = "/order_details/{order_id}"


class CommentAdd(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Comment
    form_class = CommentAddForm
    template_name = 'orders/comment_add.html'
    success_url = "/order_details/{order_id}"

    def get_initial(self):
        order_pk = self.kwargs["order_pk"]
        data = super().get_initial()
        data["order"] = Order.objects.get(pk=order_pk)
        return data


class CommentDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Comment
    success_url = "/order_details/{order_id}"


class CommentEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Comment
    form_class = CommentAddForm
    template_name_suffix = '_edit'
    success_url = "/order_details/{order_id}"


class OrderSearch(View):
    template_name = "orders/order_search.html"

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            orders = Order.objects.filter(customer__icontains=customer)
            context = {'form': form, 'orders': orders}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {'form': form})
