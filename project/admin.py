from typing import Any
from django.contrib import admin

# Register your models here.
from project.models import *

admin.site.register(Posts),
admin.site.register(Categories),
admin.site.register(bohoocatg),
admin.site.register(bohoodet),

class MasterAdmin(admin.ModelAdmin):
    list_display=['created_user','created_data','is_active']
    def save_model(self, request, obj, form, change):
        obj.created_user=request.user
        super().save_model(request, obj, form, change)

