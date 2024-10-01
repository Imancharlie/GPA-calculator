from django.contrib import admin
from .models import Credit, Electrical,Mechanical,Civil,Metallugy,Quantity,Mechanic,Industrial,Chemical,Textile

# Register your models here.
admin.site.register(Credit)
admin.site.register(Mechanical)
admin.site.register(Mechanic)
admin.site.register(Civil)
admin.site.register(Quantity)
admin.site.register(Electrical)
admin.site.register(Metallugy)
admin.site.register(Textile)
admin.site.register(Chemical)
admin.site.register(Industrial)

