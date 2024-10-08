from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Bike, BikeModel, BikeBrand, Client, Order

class BikeBrandAdmin(ImportExportModelAdmin):
    pass  # Если нет дополнительных настроек, используйте pass

class BikeModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'transmission']
    list_filter = ['brand', 'transmission']
    search_fields = ['model', 'brand__name']
    fields = ['brand', 'model', 'transmission', 'gears', 'displacement', 'fuel_system', 'tank', 'clearance', 'description', 'bike_model_photo']

class BikeAdmin(ImportExportModelAdmin):
    list_display = ['bike_model', 'amount', 'price_per_day', 'availability']
    list_filter = ['availability', 'bike_model__brand']
    search_fields = ['bike_model__brand__name', 'bike_model__model']
    readonly_fields = ['photo_preview']

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150" height="150" />')
        return "No photo"

    photo_preview.short_description = 'Photo preview'

class ClientAdmin(ImportExportModelAdmin):
    pass  # Если нет дополнительных настроек, используйте pass

class OrderAdmin(ImportExportModelAdmin):
    pass  # Если нет дополнительных настроек, используйте pass

# Register your models here.
admin.site.register(Bike, BikeAdmin)
admin.site.register(BikeModel, BikeModelAdmin)
admin.site.register(BikeBrand, BikeBrandAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
