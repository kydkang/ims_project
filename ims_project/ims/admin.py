
from django.contrib import admin
from .models import Index, Department, IndexData


class IndexAdmin(admin.ModelAdmin):
    readonly_fields=('calculated_value',)

admin.site.register(Index, IndexAdmin)
admin.site.register(Department)
admin.site.register(IndexData)