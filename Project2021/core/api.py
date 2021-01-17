from .models import Product, CategoryProduct, SubcategoryProduct, VendorProduct, Coupon, CategoryCoupon, VendorCoupon, Cashback, CategoryCashback, VendorCashback
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, CategoryProductSerializer, SubcategoryProductSerializer, VendorProductSerializer, CouponSerializer, CategoryCouponSerializer, VendorCouponSerializer, CashbackSerializer, CategoryCashbackSerializer, VendorCashbackSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoryProductSerializer

class SubcategoryProductViewSet(viewsets.ModelViewSet):
    queryset = SubcategoryProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubcategoryProductSerializer

class VendorProductViewSet(viewsets.ModelViewSet):
    queryset = VendorProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VendorProductSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CouponSerializer


class CategoryCouponViewSet(viewsets.ModelViewSet):
    queryset = CategoryCoupon.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoryCouponSerializer


class VendorCouponViewSet(viewsets.ModelViewSet):
    queryset = VendorCoupon.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VendorCouponSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    queryset = Cashback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CashbackSerializer


class CategoryCashbackViewSet(viewsets.ModelViewSet):
    queryset = CategoryCashback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoryCashbackSerializer


class VendorCashbackViewSet(viewsets.ModelViewSet):
    queryset = VendorCashback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VendorCashbackSerializer