from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    VALUATION = _('Valuation')
    NEW = _('New')
    URGENT = _('Urgent')
    DRAWING = _('Drawing')
    INCOMPLETE = _('Incomplete')
    DESIGNED = _('Designed')
    EVAULATION = _('Evaluation')
    IMPROVEMENT = _('Improvement')
    ACCEPTED = _('Accepted')
    PRODUCTION = _('Production')
    PACKED = _('Packed')
    SENT = _('Sent')
    STATUS = [
        (VALUATION, _('Valuation')),
        (NEW, _('New')),
        (URGENT, _('Urgent')),
        (DRAWING, _('Drawing')),
        (INCOMPLETE, _('Incomplete')),
        (DESIGNED, _('Designed')),
        (EVAULATION, _('Evaluation')),
        (IMPROVEMENT, _('Improvement')),
        (ACCEPTED, _('Accepted')),
        (PRODUCTION, _('Production')),
        (PACKED, _('Packed')),
        (SENT, _('Sent')),
    ]

    # Seller
    MAREK = 'Marek'
    NATALIA = 'Natalia'
    JOANNA = 'Joanna'
    SELLER = [
        (MAREK, 'Marek'),
        (NATALIA, 'Natalia'),
        (JOANNA, 'Joanna'),
    ]

    # Designer
    MIKI = 'Miki'
    OLA = 'Ola'
    DESIGNER = [
        (MIKI, 'Miki'),
        (OLA, 'Ola'),
    ]

    date = models.DateTimeField(_('date'), auto_now_add=True)
    seller = models.CharField(_('seller'), max_length=20, choices=SELLER)
    customer = models.EmailField(_('customer'), max_length=260)
    designer = models.CharField(_('designer'), max_length=20, choices=DESIGNER, default=MIKI)
    status = models.CharField(_('status'), max_length=20, choices=STATUS, default=VALUATION)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer


class Action(models.Model):
    name = models.CharField(max_length=30)
    translation = models.CharField(max_length=30)
    sequence = models.IntegerField()

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return self.name


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    # Name
    PREFAB = _('Prefab')
    NAMETAGS = _('Nametags')
    NUMBERS = _('Numbers')
    COVER = _('Covers')
    DIPLOMAS = _('Diplomas')
    STENCIL = _('Stencil')
    PLEXIGLASS = _('Plexiglass')
    CONTAINER = _('Container')
    BOARD = _('Board')
    STATUETTES = _('Statuettes')
    PLATES = _('Plates')
    LETTERS = _('Letters')

    NAME = [
        (PREFAB, _('Prefab')),
        (NAMETAGS, _('Nametags')),
        (NUMBERS, _('Numbers')),
        (COVER, _('Covers')),
        (DIPLOMAS, _('Diplomas')),
        (STENCIL, _('Stencil')),
        (PLEXIGLASS, _('Plexiglass')),
        (CONTAINER, _('Container')),
        (BOARD, _('Board')),
        (STATUETTES, _('Statuettes')),
        (PLATES, _('Plates')),
        (LETTERS, _('Letters')),
    ]

    # Material
    ALUMINIUM = _('Aluminium')
    LAMINATE = _('Laminate')
    DIBOND = _('Dibond')
    POLYCARBONATE = _('Polycarbonate')
    PLEXIGLASS = _('Plexiglass')
    CUSTOM = _('Custom')

    MATERIAL = [
        (ALUMINIUM, _('Aluminium')),
        (LAMINATE, _('Laminate')),
        (DIBOND, _('Dibond')),
        (POLYCARBONATE, _('Polycarbonate')),
        (PLEXIGLASS, _('Plexiglass')),
        (CUSTOM, _('Custom')),
    ]

    # Thickness
    ZERO_FIVE = '0,5'
    ZERO_EIGHT = '0,8'
    ONE_SIX = '1,6'
    TWO = '2'
    THREE = '3'
    FIVE = '5'
    OTHER = _('Other')

    THICKNESS = [
        (ZERO_FIVE, '0,5'),
        (ZERO_EIGHT, '0,8'),
        (ONE_SIX, '1,6'),
        (TWO, '2'),
        (THREE, '3'),
        (FIVE, '5'),
        (OTHER, _('Other')),
    ]

    # Color
    SILVER = _('Silver')
    GOLD = _('Gold')
    WHITE = _('White')
    BLACK = _('Black')
    TRANSPARENT = _('Transparent')
    CUSTOM = _('Custom')

    COLOR = [
        (SILVER, _('Silver')),
        (GOLD, _('Gold')),
        (WHITE, _('White')),
        (BLACK, _('Black')),
        (TRANSPARENT, _('Transparent')),
        (CUSTOM, _('Custom')),
    ]

    # Dimensions
    OUTSIDE = _('Outside')
    INSIDE = _('Inside')

    DIMENSIONS = [
        (OUTSIDE, _('Outside')),
        (INSIDE, _('Inside')),
    ]

    # Fastening
    PIN = _('Pin')
    MAGNET = _('Magnet')
    GLUE = _('Glue')
    HOLES = _('Holes')
    WITHOUT = _('Without')
    CUSTOM = _('Custom')

    FASTENING = [
        (PIN, _('Pin')),
        (MAGNET, _('Magnet')),
        (GLUE, _('Glue')),
        (HOLES, _('Holes')),
        (WITHOUT, _('Without')),
        (CUSTOM, _('Custom')),
    ]

    # Mark
    PRINT = _('Print')
    ENGRAVER = _('Engraver')
    FOIL = _('Foil')
    STICKER = _('Sticker')
    OUTSOURCE = _('Outsource')
    WITHOUT = _('Without')
    CUSTOM = _('Custom')

    MARK = [
        (PRINT, _('Print')),
        (ENGRAVER, _('Engraver')),
        (FOIL, _('Foil')),
        (STICKER, _('Sticker')),
        (OUTSOURCE, _('Outsource')),
        (WITHOUT, _('Without')),
        (CUSTOM, _('Custom')),
    ]
    # relacje display_name=
    name = models.CharField(_('name'), max_length=30, choices=NAME)
    material = models.CharField(_('material'), max_length=50, choices=MATERIAL)
    thickness = models.CharField(_('thickness'), max_length=10, choices=THICKNESS)
    color = models.CharField(_('color'), max_length=50, choices=COLOR)
    dimensions = models.CharField(_('dimensions'), max_length=30, choices=DIMENSIONS, null=True, blank=True, default=OUTSIDE)
    width = models.IntegerField(_('width'))
    height = models.IntegerField(_('height'))
    depth = models.IntegerField(_('depth'), null=True, blank=True)
    fastening = models.CharField(_('fastening'), max_length=30, choices=FASTENING)

    hole = models.CharField(_('hole'), max_length=20, null=True, blank=True)
    rounding = models.CharField(_('rounding'), max_length=10, null=True, blank=True)
    mark = models.CharField(_('mark'), max_length=50, choices=MARK)
    quantity = models.IntegerField(_('quantity'))
    description = models.TextField(_('description'), null=True, blank=True, default=None)

    actions = models.ManyToManyField(Action, verbose_name=_("Action"))

    def __str__(self):
        return self.name


class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.date
