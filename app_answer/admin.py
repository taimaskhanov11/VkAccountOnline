from django.contrib import admin

# Register your models here.
from app_answer.models import Category, Input, Output


class CategoryAdmin(admin.ModelAdmin):
    pass


class InputAdmin(admin.ModelAdmin):
    pass


class OutputAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Input, InputAdmin)
admin.site.register(Output, OutputAdmin)
