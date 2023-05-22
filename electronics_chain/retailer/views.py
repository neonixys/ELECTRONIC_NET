from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView

from rest_framework import permissions, filters

from electronics_chain.permissions import CustomPermissions, DestroyPermission
from electronics_chain.retailer.models import Retailer
from electronics_chain.retailer.serializers import RetailerListSerializer, RetailerDetailSerializer, \
    RetailerCreateSerializer, RetailerUpdateSerializer, RetailerDestroySerializer


class RetailerListView(ListAPIView):
    queryset = Retailer.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = RetailerListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class RetailerRetrieveView(RetrieveAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class RetailerCreateView(CreateAPIView):
    model = Retailer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = RetailerCreateSerializer


class RetailerUpdateView(UpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class RetailerDestroyView(DestroyAPIView):
    queryset = Retailer.objects.all()
    permission_classes = [DestroyPermission]
    serializer_class = RetailerDestroySerializer
