from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from network.models import Contact, NetworkNode, Product
from network.serializers import (NetworkNodeContactSerializer, NetworkNodeCreateUpdateSerializer,
                                 NetworkNodeProductSerializer, NetworkNodeSerializer)
from network.services import get_all_objects
from users.permissions import IsActiveUser


@extend_schema_view(
    list=extend_schema(description="Retrieve a list of network nodes"),
    retrieve=extend_schema(description="Retrieve a specific network node by id"),
    create=extend_schema(description="Create a new network node along its products and contact"),
    update=extend_schema(description="Update an existing network node"),
    particular_update=extend_schema(description="Particular update an existing network node"),
    destroy=extend_schema(description="Delete an existing network node"),
)
class NetworkNodeViewSet(viewsets.ModelViewSet):
    """Вьюсет для элемента сети"""

    queryset = get_all_objects(NetworkNode)
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["contact__country"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "particular_update"]:
            return NetworkNodeCreateUpdateSerializer
        return NetworkNodeSerializer


@extend_schema_view(
    list=extend_schema(description="Retrieve a list of products of network node"),
    create=extend_schema(description="Create a new product along one of network node"),
)
class NetworkNodeProductListCreateAPIView(generics.ListCreateAPIView):
    """Контроллер для создания продукта и чтения всех продуктов элемента сети"""

    serializer_class = NetworkNodeProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        network_node_pk = self.kwargs["network_node_pk"]
        return Product.objects.filter(network_node_id=network_node_pk)

    def perform_create(self, serializer):
        network_node_pk = self.kwargs["network_node_pk"]
        network_node = NetworkNode.objects.get(pk=network_node_pk)
        serializer.save(network_node=network_node)


@extend_schema_view(
    retrieve=extend_schema(description="Retrieve a specific product node by hist network node id"),
    update=extend_schema(description="Update an existing product from one network node"),
    particular_update=extend_schema(description="Particular update an existing product from one network node"),
    destroy=extend_schema(description="Delete an existing product from one network node"),
)
class NetworkNodeProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Контроллер для чтения, обновления и удаления продукта элемента сети"""

    serializer_class = NetworkNodeProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        network_node_pk = self.kwargs["network_node_pk"]
        return Product.objects.filter(network_node_id=network_node_pk)


@extend_schema_view(
    retrieve=extend_schema(description="Retrieve a specific contact node by hist network node id"),
    update=extend_schema(description="Update an existing contact from one network node"),
)
class NetworkNodeContactRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Контроллер для чтения и обновления контакта элемента сети"""

    serializer_class = NetworkNodeContactSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        network_node_pk = self.kwargs["network_node_pk"]
        return Contact.objects.filter(network_node_id=network_node_pk)
