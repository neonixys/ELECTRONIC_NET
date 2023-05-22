from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView

from electronics_chain.individual_entrepreneur.models import IndividualEntrepreneur
from electronics_chain.individual_entrepreneur.serializers import EntrepreneurListSerializer, \
    EntrepreneurDetailSerializer, EntrepreneurCreateSerializer, EntrepreneurUpdateSerializer, \
    EntrepreneurDestroySerializer
from electronics_chain.permissions import CustomPermissions, DestroyPermission


class EntrepreneurListView(ListAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = EntrepreneurListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class EntrepreneurRetrieveView(RetrieveAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = EntrepreneurDetailSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]


class EntrepreneurCreateView(CreateAPIView):
    model = IndividualEntrepreneur
    permission_classes = [CustomPermissions]
    serializer_class = EntrepreneurCreateSerializer


class EntrepreneurUpdateView(UpdateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    serializer_class = EntrepreneurUpdateSerializer


class EntrepreneurDestroyView(DestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [DestroyPermission]
    serializer_class = EntrepreneurDestroySerializer
