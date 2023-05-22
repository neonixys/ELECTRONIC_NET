from rest_framework import serializers

from electronics_chain.base.models import Products
from electronics_chain.base.serializers import ProductDetailSerializer
from electronics_chain.factory.models import FactoryStore


class FactoryStoreListSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreDetailSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)

    class Meta:
        model = FactoryStore
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "created",
        ]


class FactoryStoreUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)

    class Meta:
        model = FactoryStore
        fields = "__all__"


class FactoryStoreDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryStore
        fields = ["id"]