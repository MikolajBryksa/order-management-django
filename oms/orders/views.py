from django.shortcuts import render, redirect
from django.views import View
from .models import Order, Item, Comment, Address
from .forms import OrderAddForm, ItemAddForm, CommentAddForm, SearchForm, AddressAddForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('date').exclude(status="Sent")
        context = {"orders": orders}
        return render(request, 'orders/order_list.html', context)


class Archive(View):
    def get(self, request):
        orders_shipped = Order.objects.filter(status="Sent")
        context = {"orders_shipped": orders_shipped}
        return render(request, 'orders/archive.html', context)


class Stats(View):
    def get(self, request):
        marek = Order.objects.filter(seller="Marek").exclude(status="Sent").count()
        natalia = Order.objects.filter(seller="Natalia").exclude(status="Sent").count()
        joanna = Order.objects.filter(seller="Joanna").exclude(status="Sent").count()
        ania = Order.objects.filter(seller="Ania").exclude(status="Sent").count()
        miki = Order.objects.filter(designer='Miki').filter(
            Q(status='New') | Q(status='Urgent') | Q(status='Drawing') | Q(status='Incomplete') | Q(
                status='Improvement')).count()
        ola = Order.objects.filter(designer='Ola').filter(
            Q(status='New') | Q(status='Urgent') | Q(status='Drawing') | Q(status='Incomplete') | Q(
                status='Improvement')).count()
        context = {"marek": marek, "natalia": natalia, "joanna": joanna, "ania": ania, "miki": miki, "ola": ola}
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


class AddressDetails(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, order_pk):
        order = Order.objects.get(pk=order_pk)
        try:
            address = Address.objects.get(order=order_pk)
        except:
            address = None

        context = {"order": order, "address": address}
        return render(request, 'orders/address_details.html', context)


class AddressAdd(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Address
    form_class = AddressAddForm
    template_name = 'orders/address_add.html'
    success_url = "/address_details/{order_id}"

    def get_initial(self):
        order_pk = self.kwargs["order_pk"]
        data = super().get_initial()
        data["order"] = Order.objects.get(pk=order_pk)
        return data


class AddressDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Address
    success_url = "/address_details/{order_id}"


class AddressEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Address
    form_class = AddressAddForm
    template_name_suffix = '_edit'
    success_url = "/address_details/{order_id}"
