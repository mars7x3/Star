from django.contrib import admin
from .models import *


admin.site.register(Star)
admin.site.register(StarComment)
admin.site.register(StarWork)
admin.site.register(Toast)
admin.site.register(Orders)


@admin.register(StarCategory)
class StarCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ToastCategory)
class ToastCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
