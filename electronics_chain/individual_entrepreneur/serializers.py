from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from electronics_chain.base.models import Products
from electronics_chain.factory.models import FactoryStore
from electronics_chain.individual_entrepreneur.models import IndividualEntrepreneur
from electronics_chain.retailer.models import Retailer


class EntrepreneurListSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field='title'
    )
    supplier = serializers.CharField(allow_null=True)

    class Meta:
        model = IndividualEntrepreneur
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


class EntrepreneurDetailSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Products.objects.all(),
        slug_field="title"
    )
    supplier = serializers.CharField(
        required=False,
        allow_null=True,
    )

    class Meta:
        model = IndividualEntrepreneur
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


class EntrepreneurCreateSerializer(serializers.ModelSerializer):
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
    supplier = serializers.CharField(required=False)
    credit = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = IndividualEntrepreneur
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
        supplier = validated_data.pop("supplier")

        with transaction.atomic():
            entrepreneur = IndividualEntrepreneur.objects.create(
                title=validated_data.get("title"),
                email=validated_data.get("email"),
                city=validated_data.get("city"),
                credit=validated_data.get("credit")
            )

            try:
                supplier_object = FactoryStore.objects.filter(title=supplier).first() \
                                  or Retailer.objects.get(title=supplier)
                entrepreneur.supplier = supplier_object
                entrepreneur.save()
            except FactoryStore.DoesNotExist and Retailer.DoesNotExist:
                raise ValidationError(f"Поставщик {supplier} не найден")

            supplier_products = [product.title for product in supplier_object.products.all()]

            for product in validated_data.get("products"):
                if product.title in supplier_products:
                    product_obj = Products.objects.get(title=product)
                    entrepreneur.products.add(product_obj)
                    entrepreneur.save()
                else:
                    raise ValidationError(
                        f"У поставщика нет продукта {product.title}"
                    )

        return entrepreneur


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
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
    supplier = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = IndividualEntrepreneur
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


class EntrepreneurDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = ["id"]
