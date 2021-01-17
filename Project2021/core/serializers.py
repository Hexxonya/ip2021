from rest_framework import serializers
from .models import Product, CategoryProduct, SubcategoryProduct, VendorProduct, Coupon, CategoryCoupon, VendorCoupon, Cashback, CategoryCashback, VendorCashback


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'


class SubcategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoryProduct
        fields = '__all__'


class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProduct
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CategoryCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCoupon
        fields = '__all__'


class VendorCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCoupon
        fields = '__all__'


class CashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = '__all__'


class CategoryCashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCashback
        fields = '__all__'


class VendorCashbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCashback
        fields = '__all__'





