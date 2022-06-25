from django.contrib import admin

from .models  import *

class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talle', 'color', 'precio')
    search_fields = ('marca', 'talle', 'color')

admin.site.register(Remera, RemeraAdmin)

class PantalonAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talle', 'color', 'precio')
    search_fields = ('marca', 'talle', 'color')

admin.site.register(Pantalon, PantalonAdmin)

class CamisaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talle', 'color', 'precio')
    search_fields = ('marca', 'talle', 'color')
    
admin.site.register(Camisa, CamisaAdmin)
