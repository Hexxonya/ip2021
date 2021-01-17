from rest_framework import routers
from .api import ProductViewSet, CategoryProductViewSet, SubcategoryProductViewSet, VendorProductViewSet, CouponViewSet, CategoryCouponViewSet, VendorCouponViewSet, CashbackViewSet, CategoryCashbackViewSet, VendorCashbackViewSet

router = routers.DefaultRouter()
router.register('api/product', ProductViewSet, 'product')
router.register('api/categoryproduct', CategoryProductViewSet, 'categoryproduct')
router.register('api/subcategoryproduct', SubcategoryProductViewSet, 'subcategoryproduct')
router.register('api/vendorproduct', VendorProductViewSet, 'vendorproduct')
router.register('api/coupon', CouponViewSet, 'coupon')
router.register('api/categorycoupon', CategoryCouponViewSet, 'categorycoupon')
router.register('api/vendorcoupon', VendorCouponViewSet, 'vendorcoupon')
router.register('api/cashback', CashbackViewSet, 'cashback')
router.register('api/categorycashback', CategoryCashbackViewSet, 'categorycashback')
router.register('api/vendorcashback', VendorCashbackViewSet, 'vendorcashback')


urlpatterns = router.urls