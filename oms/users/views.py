from .forms import LoginForm, UserAddForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, RedirectView
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

User = get_user_model()


class UserList(ListView):
    model = User
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

# class SetPass(UpdateView):
#     template_name = 'users/user_login.html'
#     model = User
#     fields = ['username', 'password']
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         self.object.set_password(form.cleaned_data['password'])
#         self.object.save()
#         return super().form_valid(form)
