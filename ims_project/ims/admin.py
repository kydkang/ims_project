
from django.contrib import admin
from .models import Dname_Indexname

admin.site.register(Dname_Indexname)

# class MyModelAdmin(admin.ModelAdmin):
#     readonly_fields=('first',)