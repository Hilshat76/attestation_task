from rest_framework import serializers
from .models import NetworkNode, Product


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "name",
            "contact_email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier_node",
            "debt",
            "created_at",
        ]

    def update(self, instance, validated_data):
        # Проверяем, пытаются ли обновить поле "debt"
        if "debt" in validated_data:
            raise serializers.ValidationError(
                {"debt": "Нельзя изменять задолженность через API."}
            )

        return super().update(instance, validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "model",
            "release_date",
            "network_node",
        ]
