
from rest_framework import serializers

from electronics_chain.base.models import Products


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    product_model = serializers.CharField(required=False)

    class Meta:
        model = Products
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    product_model = serializers.CharField()

    class Meta:
        model = Products
        fields = "__all__"


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id"]


