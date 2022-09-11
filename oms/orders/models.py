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
    customer = models.EmailField(max_length=260)
    designer = models.CharField(max_length=20, choices=DESIGNER)
    status = models.CharField(max_length=20, choices=STATUS, default=NEW)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    # Name
    CARD = 'Card'
    CONTAINER = 'Container'
    SIGNBOARD = 'Signboard'

    NAME = [
        (CARD, 'Card'),
        (CONTAINER, 'Container'),
        (SIGNBOARD, 'Signboard'),
    ]

    # Material
    ALUMINIUM = 'Aluminium'
    LAMINATE = 'Laminate'
    DIBOND = 'Dibond'
    POLYCARBONATE = 'Polycarbonate'
    PLEXI = 'Plexi'
    CUSTOM = 'Custom'

    MATERIAL = [
        (ALUMINIUM, 'Aluminium'),
        (LAMINATE, 'Laminate'),
        (DIBOND, 'Dibond'),
        (POLYCARBONATE, 'Polycarbonate'),
        (PLEXI, 'Plexi'),
        (CUSTOM, 'Custom'),
    ]

    # Thickness
    ZERO_FIVE = '0,5'
    ZERO_EIGHT = '0,8'
    ONE_SIX = '1,6'
    TWO = '2'
    THREE = '3'
    FIVE = '5'
    OTHER = 'Other'

    THICKNESS = [
        (ZERO_FIVE, '0,5'),
        (ZERO_EIGHT, '0,8'),
        (ONE_SIX, '1,6'),
        (TWO, '2'),
        (THREE, '3'),
        (FIVE, '5'),
        (OTHER, 'Other'),
    ]

    # Color
    SILVER = 'Silver'
    GOLD = 'Gold'
    WHITE = 'White'
    BLACK = 'Black'
    TRANSPARENT = 'Transparent'
    CUSTOM = 'Custom'

    COLOR = [
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (TRANSPARENT, 'Transparent'),
        (CUSTOM, 'Custom'),
    ]

    # Dimensions
    OUTSIDE = 'Outside'
    INSIDE = 'Inside'

    DIMENSIONS = [
        (OUTSIDE, 'Outside'),
        (INSIDE, 'Inside'),
    ]

    # Fastening
    PIN = 'Pin'
    MAGNET = 'Magnet'
    GLUE = 'Glue'
    HOLES = 'Holes'
    WITHOUT = 'Without'
    CUSTOM = 'Custom'

    FASTENING = [
        (PIN, 'Pin'),
        (MAGNET, 'Magnet'),
        (GLUE, 'Glue'),
        (HOLES, 'Holes'),
        (WITHOUT, 'Without'),
        (CUSTOM, 'Custom'),
    ]

    # Mark
    PRINT = 'Print'
    ENGRAVER = 'Engraver'
    FOIL = 'Foil'
    STICKER = 'Sticker'
    WITHOUT = 'Without'
    CUSTOM = 'Custom'

    MARK = [
        (PRINT, 'Print'),
        (ENGRAVER, 'Engraver'),
        (FOIL, 'Foil'),
        (STICKER, 'Sticker'),
        (WITHOUT, 'Without'),
        (CUSTOM, 'Custom'),
    ]

    name = models.CharField(max_length=30, choices=NAME)
    material = models.CharField(max_length=50, choices=MATERIAL)
    thickness = models.CharField(max_length=10, choices=THICKNESS)
    color = models.CharField(max_length=50, choices=COLOR)
    dimensions = models.CharField(max_length=30, choices=DIMENSIONS, null=True, blank=True, default=OUTSIDE)
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField(null=True, blank=True)
    fastening = models.CharField(max_length=30, choices=FASTENING)

    hole = models.CharField(max_length=20, null=True, blank=True)
    rounding = models.CharField(max_length=10, null=True, blank=True)
    mark = models.CharField(max_length=50, choices=MARK)
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
