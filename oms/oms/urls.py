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
from django.urls import path

from orders.views import OrderList, OrderDetails, OrderAdd, OrderEdit, OrderDelete, ItemAdd, ItemEdit, ItemDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrderList.as_view(), name='order_list'),
    path('order_details/<int:order_pk>/', OrderDetails.as_view(), name='order_details'),

    path('order_add/', OrderAdd.as_view(), name='order_add'),
    path('order_edit/<pk>/', OrderEdit.as_view(), name="order_edit"),
    path('order_delete/<pk>/', OrderDelete.as_view(), name="order_delete"),

    path('item_add/', ItemAdd.as_view(), name='item_add'),
    path('item_edit/<pk>/', ItemEdit.as_view(), name="item_edit"),
    path('item_delete/<pk>/', ItemDelete.as_view(), name="item_delete"),

]
