from django.contrib import admin
from backend.models import Bicycle, BoolType


@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'time_created', 'is_published', 'is_available')
    list_display_links = ('id', 'name')
    ordering = ('time_created', 'name')
    list_editable = ('is_published', 'is_available',)
    # raw_id_fields = ('category',)
    list_per_page = 3
    actions = ['set_published', 'unpublish', 'make_available', 'make_unavailable']
    search_fields = ['name']
    list_filter = ['category__name', 'is_published']

    @admin.action(description='Publish')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=BoolType.YES)
        self.message_user(request, 'Updated %d bicycles.' % count)

    @admin.action(description='Unpublish')
    def unpublish(self, request, queryset):
        count = queryset.update(is_published=BoolType.NO)
        self.message_user(request, 'Updated %d bicycles.' % count)

    @admin.action(description='Make available')
    def make_available(self, request, queryset):
        count = queryset.update(is_available=BoolType.YES)
        self.message_user(request, 'Updated %d bicycles.' % count)

    @admin.action(description='Make unavailable')
    def make_unavailable(self, request, queryset):
        count = queryset.update(is_available=BoolType.NO)
        self.message_user(request, 'Updated %d bicycles.' % count)

# admin.site.register(Bicycle, BicycleAdmin)
# Register your models here.
