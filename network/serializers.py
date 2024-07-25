from rest_framework import serializers

from network.models import Contact, NetworkNode, Product
from network.services import create_products_and_contact, update_products_and_contact


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для контакта"""

    class Meta:
        model = Contact
        fields = ("id", "email", "country", "city", "street", "house_number")


class ContactCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания контакта"""

    class Meta:
        model = Contact
        fields = ("email", "country", "city", "street", "house_number")


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продукта"""

    class Meta:
        model = Product
        fields = ("id", "title", "model", "on_market")


class ProductCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания продукта"""

    class Meta:
        model = Product
        fields = ("title", "model", "on_market")


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для элемента сети"""

    contact = ContactSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = "__all__"
        read_only_fields = ["debt", "created_at"]


class NetworkNodeCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления элемента сети"""

    contact = ContactCreateSerializer()
    products = ProductCreateSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = ("name", "level", "supplier", "debt", "contact", "products")
        read_only_fields = ["debt", "created_at"]

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        contact_data = validated_data.pop("contact")

        network_node = NetworkNode.objects.create(**validated_data)

        create_products_and_contact(Product, Contact, products_data, contact_data, network_node)

        return network_node

    def update(self, instance, validated_data):
        products_data = validated_data.pop("products")
        contact_data = validated_data.pop("contact")

        instance.name = validated_data.get("name", instance.name)
        instance.level = validated_data.get("level", instance.level)
        instance.supplier = validated_data.get("supplier", instance.supplier)
        instance.save()

        update_products_and_contact(Product, Contact, products_data, contact_data, instance)

        return instance


class NetworkNodeProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов конкретного элемента сети"""

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["network_node"]


class NetworkNodeContactSerializer(serializers.ModelSerializer):
    """Сериализатор для контакта конкретного элемента сети"""

    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ["network_node"]
