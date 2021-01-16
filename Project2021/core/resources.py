from import_export import resources
from .models import Product, CategoryProduct, SubcategoryProduct, VendorProduct, Coupon, CategoryCoupon, VendorCoupon, Cashback, CategoryCashback, VendorCashback

class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


class CategoryProductResource(resources.ModelResource):

    class Meta:
        model = CategoryProduct


class SubcategoryProductResource(resources.ModelResource):

    class Meta:
        model = SubcategoryProduct


class VendorProductResource(resources.ModelResource):

    class Meta:
        model = VendorProduct


class CouponResource(resources.ModelResource):

    class Meta:
        model = Coupon


class CategoryCouponResource(resources.ModelResource):

    class Meta:
        model = CategoryCoupon


class VendorCouponResource(resources.ModelResource):

    class Meta:
        model = VendorCoupon


class CashbackResource(resources.ModelResource):

    class Meta:
        model = Cashback


class CategoryCashbackResource(resources.ModelResource):

    class Meta:
        model = CategoryCashback


class VendorCashbackResource(resources.ModelResource):

    class Meta:
        model = VendorCashback