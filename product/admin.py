from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Warehouse)
admin.site.register(WarehouseItem)
