from django.contrib import admin

from .models  import *

class RemeraAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'talle', 'color', 'precio')
    search_fields = ('modelo', 'talle', 'color')

admin.site.register(Remera, RemeraAdmin)

class PantalonAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'talle', 'color', 'precio')
    search_fields = ('modelo', 'talle', 'color')

admin.site.register(Pantalon, PantalonAdmin)

class CamisaAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'talle', 'color', 'precio')
    search_fields = ('modelo', 'talle', 'color')
    
admin.site.register(Camisa, CamisaAdmin)

admin.site.register(Avatar)