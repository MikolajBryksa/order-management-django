"""oms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

from orders.views import OrderList, OrderDetails, OrderAdd, OrderEdit, OrderDelete, \
    ItemAdd, ItemEdit, ItemDelete, CommentAdd, CommentEdit, CommentDelete, Info, Stats, OrderSearch

from users.views import UserList, Login, Logout, UserAdd, UserEdit, UserDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Language
urlpatterns += i18n_patterns(
    path('', OrderList.as_view(), name='order_list'),

    path('stats/', Stats.as_view(), name='stats'),
    path('info/', Info.as_view(), name='info'),
    path('order_details/<int:order_pk>/', OrderDetails.as_view(), name='order_details'),
    path('order_search/', OrderSearch.as_view(), name='order_search'),

    path('order_add/', OrderAdd.as_view(), name='order_add'),
    path('order_edit/<int:pk>/', OrderEdit.as_view(), name="order_edit"),
    path('order_delete/<int:pk>/', OrderDelete.as_view(), name="order_delete"),

    path('item_add/<int:order_pk>/', ItemAdd.as_view(), name='item_add'),
    path('item_edit/<int:pk>/', ItemEdit.as_view(), name="item_edit"),
    path('item_delete/<int:pk>/', ItemDelete.as_view(), name="item_delete"),

    path('comment_add/<int:order_pk>/', CommentAdd.as_view(), name='comment_add'),
    path('comment_edit/<int:pk>/', CommentEdit.as_view(), name="comment_edit"),
    path('comment_delete/<int:pk>/', CommentDelete.as_view(), name="comment_delete"),

    path('user_list/', UserList.as_view(), name="user_list"),
    path('user_add/', UserAdd.as_view(), name="user_add"),
    path('user_edit/<int:pk>/', UserEdit.as_view(), name="user_edit"),
    path('user_delete/<int:pk>/', UserDelete.as_view(), name="user_delete"),

    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),

)
