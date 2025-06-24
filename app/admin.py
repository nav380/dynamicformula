from django.contrib import admin
from .models import Formula

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ('name', 'expression')
    search_fields = ('name',)
    list_filter = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'expression', 'variables')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['variables']
        return super().get_readonly_fields(request, obj)    
