from django.contrib import admin
from Properties.models import Building, Amenity, Tenant, TotalTenants, Caretaker

# Register your models here.

admin.site.register(Building)
admin.site.register(Amenity)
admin.site.register(Tenant)
admin.site.register(TotalTenants)
admin.site.register(Caretaker)

