from django.contrib import admin
from .models import *

# Register your models here.

class RifaAdmin(admin.ModelAdmin):
    list_display = ['id','vendedor','comprador','fecha_creacion']
    list_display_links = ['id','vendedor','comprador','fecha_creacion']
    search_fields = ['comprador', 'vendedor']
    list_filter = ['vendedor']

class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nombre','rifas_vendidas','curso']
    list_display_links = ['nombre','rifas_vendidas','curso']
    search_fields = ['nombre']
    list_filter = ['curso']



admin.site.register(Rifa, RifaAdmin)
admin.site.register(Vendedor, VendedorAdmin)
