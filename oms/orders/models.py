from django.db import models


class Order(models.Model):
    # Status
    NEW = 'New'
    URGENT = 'Urgent'
    DRAWING = 'Drawing'
    INCOMPLETE = 'Incomplete'
    DESIGNED = 'Designed'
    EVAULATION = 'Evaluation'
    IMPROVEMENT = 'Improvement'
    ACCEPTED = 'Accepted'
    PRODUCTION = 'Production'
    PACKED = 'Packed'
    SENT = 'Sent'

    STATUS = [
        (NEW, 'New'),
        (URGENT, 'Urgent'),
        (DRAWING, 'Drawing'),
        (INCOMPLETE, 'Incomplete'),
        (DESIGNED, 'Designed'),
        (EVAULATION, 'Evaluation'),
        (IMPROVEMENT, 'Improvement'),
        (ACCEPTED, 'Accepted'),
        (PRODUCTION, 'Production'),
        (PACKED, 'Packed'),
        (SENT, 'Sent'),
    ]

    # Seller
    MARK = 'Mark'
    NATALIE = 'Natalie'
    JOANNA = 'Joanna'

    SELLER = [
        (MARK, 'Mark'),
        (NATALIE, 'Natalie'),
        (JOANNA, 'Joanna'),
    ]

    # Designer
    MIKI = 'Miki'
    OLA = 'Ola'

    DESIGNER = [
        (MIKI, 'Miki'),
        (OLA, 'Ola'),
    ]

    date = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=20, choices=SELLER)
    customer = models.EmailField(max_length=254)
    designer = models.CharField(max_length=20, choices=DESIGNER)
    status = models.CharField(max_length=20, choices=STATUS, default=NEW)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer
