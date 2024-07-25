from django.contrib import admin
from django.utils.html import format_html

from network.models import Contact, NetworkNode, Product


class ContactInLine(admin.StackedInline):
    """Инлайн для контактов"""

    model = Contact
    extra = 1


class ProductInLine(admin.StackedInline):
    """Инлайн для продуктов"""

    model = Product
    extra = 1


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """Админка для элемента сети"""

    list_display = ("name", "supplier_link", "city", "debt")
    list_filter = ("contact__city",)
    search_fields = ("name", "contact__city")
    inlines = [ContactInLine, ProductInLine]
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            supplier_url = '<a href="/admin/network/networknode/{}/change/">{}</a>'
            return format_html(supplier_url, obj.supplier.id, obj.supplier.name)
        return "-"

    supplier_link.allow_tags = True
    supplier_link.short_description = "Поставщик"

    def city(self, obj):
        return obj.contact.city if obj.contact else "-"

    city.short_description = "Город"
