from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView

from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from electronics_chain.factory.models import FactoryStore
from electronics_chain.factory.serializers import FactoryStoreListSerializer, FactoryStoreDetailSerializer, \
    FactoryStoreCreateSerializer, FactoryStoreUpdateSerializer, FactoryStoreDestroySerializer
from electronics_chain.permissions import CustomPermissions, DestroyPermission


class FactoryStoreListView(ListAPIView):
    queryset = FactoryStore.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = FactoryStoreListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title"]
    ordering = ["title"]


class FactoryStoreRetrieveView(RetrieveAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class FactoryStoreCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = FactoryStoreCreateSerializer


class FactoryStoreUpdateView(UpdateAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class FactoryStoreDestroyView(DestroyAPIView):
    queryset = FactoryStore.objects.all()
    serializer_class = FactoryStoreDestroySerializer
    permission_classes = [DestroyPermission]


