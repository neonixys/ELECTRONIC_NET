from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from electronics_chain.base.models import Products
from electronics_chain.base.serializers import ProductDetailSerializer
from electronics_chain.factory.models import FactoryStore
from electronics_chain.factory.serializers import FactoryStoreDetailSerializer
from electronics_chain.retailer.models import Retailer


class RetailerListSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True)
    supplier = FactoryStoreDetailSerializer(allow_null=True)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerDetailSerializer(serializers.ModelSerializer):
    products = ProductDetailSerializer(many=True, read_only=True)
    supplier = FactoryStoreDetailSerializer(allow_null=True)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field='title'
    )
    email = serializers.CharField()
    country = serializers.CharField(required=False)
    city = serializers.CharField()
    street = serializers.CharField(required=False)
    house = serializers.IntegerField(required=False)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=FactoryStore.objects.all(),
        required=False,
        allow_null=True
    )
    credit = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Retailer
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]

    def create(self, validated_data):
        supplier = FactoryStore.objects.get(id=validated_data.get("supplier").id)
        supplier_products = [product.title for product in supplier.products.all()]

        with transaction.atomic():
            retailer = Retailer.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                supplier=supplier,
                credit=validated_data.get("credit")
            )

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Products.objects.get(title=product)
                    retailer.products.add(product_obj)
                    retailer.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return retailer


class RetailerUpdateSerializer(serializers.ModelSerializer):
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
    supplier = serializers.PrimaryKeyRelatedField(
        required=False,
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Retailer
        read_only_fields = ["credit"]
        fields = [
            "id",
            "title",
            "email",
            "country",
            "city",
            "street",
            "house",
            "products",
            "supplier",
            "credit",
            "created",
        ]


class RetailerDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ["id"]
