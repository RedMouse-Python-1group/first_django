from django.contrib import admin

# Register your models here.
from .models import App

def make_published(modeladmin, request, queryset):
    for q in queryset:
        q.enable = not q.enable
        q.save()

make_published.short_description = "Revers enable"


class AppAdmin (admin.ModelAdmin):
    actions_on_bottom = True
    actions = [make_published]
    # fields = ('field2', 'field1')
    fieldsets = (
        ("Base", {
            'fields': ('field1', 'field2')
        }),
        ('Advanced options', {
            # 'classes': ('collapse',),
            'fields': ('enable',)
        }),
    )
    list_display = ('field1', 'field2', 'enable')
    list_display_links = ('field1', 'field2')
    list_editable = ('enable',)
    list_filter = ('enable',)
    list_max_show_all = 3
    list_per_page = 3
    readonly_fields = ('field1', 'field2')
    search_fields = ('field1', 'field2')
    view_on_site = True

    def save_model(self, request, obj, form, change):
        obj.field1 = obj.field1 +'1212'
        obj.save()

admin.site.register(App, AppAdmin)
admin.site.disable_action('delete_selected')
