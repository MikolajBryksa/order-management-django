import pytest
from orders.models import Order
# from orders.views import Stats
from django.urls import reverse


# pytest -rP


@pytest.mark.skip
def test_example():
    assert 1 == 1


def test_user_name(user_1):
    print(user_1)
    assert user_1.username == "test-user"


# @pytest.mark.django_db
def test_create_order(order_1):
    print(order_1)
    assert order_1.customer == "new_customer@test.com"


def test_update_order(order_1):
    order = order_1
    order.customer = "different_customer@test.com"
    order.save()
    order_from_db = Order.objects.get(customer="different_customer@test.com")
    print(order_from_db)
    assert order_from_db.customer == "different_customer@test.com"


def test_stats(db):
    order1 = Order.objects.create(seller="Natalia", customer="first_customer@test.com", status="New")
    order2 = Order.objects.create(seller="Natalia", customer="second_customer@test.com", status="New")
    order3 = Order.objects.create(seller="Natalia", customer="third_customer@test.com", status="Sent")

    # Replace the line below (from views)
    natalia = Order.objects.filter(seller="Natalia").exclude(status="Sent").count()
    assert natalia == 2


# client = web browser
@pytest.mark.django_db
def test_view(client):
    url = reverse('order_list')
    response = client.get(url)
    assert response.status_code == 200
