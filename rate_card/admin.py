from django.contrib import admin
from .models import RateCard, BusinessModel, ServiceCategory, ServiceArea

# Register your models here.
admin.site.register(RateCard)
admin.site.register(BusinessModel)
admin.site.register(ServiceCategory)
admin.site.register(ServiceArea)
