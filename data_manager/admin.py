from django.contrib import admin
from .models import Case, Masspoint


class MasspointInline(admin.TabularInline):
    model = Masspoint
    extra = 1


class CaseAdmin(admin.ModelAdmin):
    list_display = {'name', 'description'}

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Axes', {'fields': ['label_x_min', 'label_x_max', 'label_y_min', 'label_y_max', 'label_z_min', 'label_z_max'],
                  'classes': ['collapse']}),
    ]

    inlines = [MasspointInline]


admin.site.register(Case, CaseAdmin),
admin.site.register(Masspoint)