from django.contrib import admin
from django.utils.html import format_html
from .models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country", "supplier_link", "debt", "created_at")
    list_filter = ("city",)  # Фильтр по названию города
    search_fields = ("name", "city", "country")  # Поиск по названию и местоположению
    actions = ["clear_debt"]  # Добавляем кастомный action

    def supplier_link(self, obj):
        """Создание кликабельной ссылки на поставщика"""

        if obj.supplier_node:
            # Предполагается домен http://127.0.0.1:8000/
            api_url = f"http://127.0.0.1:8000/api/network-nodes/{obj.supplier_node.id}/"

            return format_html(
                '<a href="{}">{}</a>',
                api_url,
                obj.supplier_node.name,
            )
        return "—"

    supplier_link.short_description = "Поставщик"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        """Обнуление задолженности у выбранных объектов"""

        queryset.update(debt=0.00)
        self.message_user(request, "Задолженность успешно обнулена!")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date", "get_network_nodes")
    search_fields = ("name", "model")

    def get_network_nodes(self, obj):
        """Возвращает список поставщиков через запятую"""
        return ", ".join([node.name for node in obj.network_node.all()])

    get_network_nodes.short_description = "Доступно в"  # Название колонки в админке
