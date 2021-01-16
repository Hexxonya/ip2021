from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource, CategoryProductResource, SubcategoryProductResource, VendorProductResource, CouponResource, CategoryCouponResource, VendorCouponResource, CashbackResource, CategoryCashbackResource, VendorCashbackResource
from .models import Product, CategoryProduct, SubcategoryProduct, VendorProduct, Coupon, CategoryCoupon, VendorCoupon, Cashback, CategoryCashback, VendorCashback


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "categoryProduct", "subcategoryProduct", "vendorProduct", "description", "discount", "price", "get_sale", "check")
    list_filter = ("categoryProduct", "subcategoryProduct", "vendorProduct", "discount",)
    search_fields = ("name__startswith",)

    resource_class = ProductResource

    model = Product
    actions = ['make_bad']

    def make_bad(self, request, queryset):
        queryset.update( check = False)


@admin.register(SubcategoryProduct)
class SubcategoryProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "categoryProduct", "view_products_link")

    resource_class = SubcategoryProductResource

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:core_product_changelist")
                + "?"
                + urlencode({"categorys__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)

    view_products_link.short_description = "Products"


@admin.register(CategoryProduct)
class CategoryProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_products_link")

    resource_class = CategoryProductResource

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:core_product_changelist")
                + "?"
                + urlencode({"categoryProducts__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)

    view_products_link.short_description = "Products"


@admin.register(VendorProduct)
class VendorProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_products_link")

    resource_class = VendorProductResource

    def view_products_link(self, obj):
        count = obj.product_set.count()
        url = (
                reverse("admin:core_product_changelist")
                + "?"
                + urlencode({"categoryProducts__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)

    view_products_link.short_description = "Products"


@admin.register(Coupon)
class CouponAdmin(ImportExportModelAdmin):
    list_display = ("name", "categoryCoupon", "vendorCoupon", "description", "code")
    list_filter = ("categoryCoupon", "vendorCoupon")
    search_fields = ("name__startswith",)

    resource_class = CouponResource


@admin.register(CategoryCoupon)
class CategoryCouponAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_coupons_link")

    resource_class = CategoryCouponResource

    def view_coupons_link(self, obj):
        count = obj.coupon_set.count()
        url = (
                reverse("admin:core_coupon_changelist")
                + "?"
                + urlencode({"categoryCoupons__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Coupons</a>', url, count)

    view_coupons_link.short_description = "Coupons"


@admin.register(VendorCoupon)
class VendorCouponAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_coupons_link")

    resource_class = VendorCouponResource

    def view_coupons_link(self, obj):
        count = obj.coupon_set.count()
        url = (
                reverse("admin:core_coupon_changelist")
                + "?"
                + urlencode({"categoryCoupons__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Coupons</a>', url, count)

    view_coupons_link.short_description = "Coupons"


@admin.register(Cashback)
class CashbackAdmin(ImportExportModelAdmin):
    list_display = ("name", "categoryCashback", "vendorCashback", "description", "ref")
    list_filter = ("categoryCashback", "vendorCashback")
    search_fields = ("name__startswith",)

    resource_class = CashbackResource


@admin.register(CategoryCashback)
class CategoryCashbackAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_cashbacks_link")

    resource_class = CategoryCashbackResource

    def view_cashbacks_link(self, obj):
        count = obj.cashback_set.count()
        url = (
                reverse("admin:core_cashback_changelist")
                + "?"
                + urlencode({"categoryCashbacks__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Cashbacks</a>', url, count)

    view_cashbacks_link.short_description = "Cashbacks"


@admin.register(VendorCashback)
class VendorCashbackAdmin(ImportExportModelAdmin):
    list_display = ("name", "view_cashbacks_link")

    resource_class = VendorCashbackResource

    def view_cashbacks_link(self, obj):
        count = obj.cashback_set.count()
        url = (
                reverse("admin:core_cashback_changelist")
                + "?"
                + urlencode({"categoryСashbacks__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Сashbacks</a>', url, count)

    view_cashbacks_link.short_description = "Сashbacks"