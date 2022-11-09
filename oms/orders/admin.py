from django.contrib import admin
from .models import Order, Action, Item, Comment, Address

admin.site.register(Order)
admin.site.register(Action)
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Address)

