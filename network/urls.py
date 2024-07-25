from django.urls import include, path
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import (NetworkNodeContactRetrieveUpdateAPIView, NetworkNodeProductListCreateAPIView,
                           NetworkNodeProductRetrieveUpdateDestroyAPIView, NetworkNodeViewSet)

app_name = NetworkConfig.name

router = DefaultRouter()

router.register(r"nodes", NetworkNodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "nodes/<int:network_node_pk>/products/",
        NetworkNodeProductListCreateAPIView.as_view(),
        name="create_list_product",
    ),
    path(
        "nodes/<int:network_node_pk>/products/<int:pk>/",
        NetworkNodeProductRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve_update_destroy_product",
    ),
    path(
        "nodes/<int:network_node_pk>/contact/<int:pk>/",
        NetworkNodeContactRetrieveUpdateAPIView.as_view(),
        name="retrieve_update_contact",
    ),
]
