from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from electronics_chain.base.models import Products
from electronics_chain.base.serializers import ProductCreateSerializer, ProductsListSerializer, ProductDetailSerializer, \
    ProductUpdateSerializer, ProductDestroySerializer
from electronics_chain.permissions import CustomPermissions


class ProductsCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = ProductCreateSerializer


class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = ProductsListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]


class ProductRetrieveView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class ProductUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class ProductDestroyView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductDestroySerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]