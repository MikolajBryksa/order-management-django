from .forms import LoginForm, UserAddForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, RedirectView, DeleteView, UpdateView
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

User = get_user_model()


class UserList(ListView):
    # model = User
    queryset = User.objects.order_by("groups__name")
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class Login(FormView):
    template_name = 'users/user_login.html'
    success_url = reverse_lazy('order_list')
    form_class = LoginForm

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)


class Logout(RedirectView):
    url = reverse_lazy('order_list')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class UserAdd(PermissionRequiredMixin, CreateView):
    permission_required = 'users.add_user'
    model = User
    template_name = 'users/user_add.html'
    form_class = UserAddForm
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password1'])
        self.object.save()
        return response


class UserDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.delete_user'
    model = User
    success_url = reverse_lazy('user_list')


class UserEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = User
    form_class = UserAddForm
    template_name_suffix = '_edit'
    success_url = reverse_lazy('user_list')
