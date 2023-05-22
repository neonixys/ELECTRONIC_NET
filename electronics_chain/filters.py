from django_filters import rest_framework

from electronics_chain.factory.models import FactoryStore


class CountryFilter(rest_framework.FilterSet):
    class Meta:
        model = FactoryStore
        fields = ("country",)
