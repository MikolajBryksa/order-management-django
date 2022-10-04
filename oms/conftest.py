import pytest
from django.contrib.auth.models import User
from orders.models import Order


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    return user


@pytest.fixture()
def order_1(db):
    order = Order.objects.create(customer="new_customer@test.com")
    return order
