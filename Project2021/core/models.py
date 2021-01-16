from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CategoryProduct(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Category Product"


class SubcategoryProduct(models.Model):
    name = models.CharField('Name', max_length=50)
    categoryProduct = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Subcategory"


class VendorProduct(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Vendor Product"


class Product(models.Model):
    name = models.CharField('Name', max_length=50)
    categoryProduct = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    subcategoryProduct = models.ForeignKey(SubcategoryProduct, on_delete=models.CASCADE)
    vendorProduct = models.ForeignKey(VendorProduct, on_delete=models.CASCADE)
    description = models.TextField('Description',)
    discount = models.IntegerField('Discount', validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.IntegerField('Price',)
    check = models.BooleanField(default=True)

    def get_sale(self):
        price = self.price - (self.price * (self.discount/100))
        return price

    get_sale.short_description = "Sale"

    # def __str__(self):
    #     return f"{self.name}, {self.category}, {self.vendor}, {self.description}, {self.discount}, {self.price}, {self.get_sale()}"

    class Meta:
        verbose_name_plural = "Product"


class CategoryCoupon(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Category Coupon"


class VendorCoupon(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Vendor Coupon"


class Coupon(models.Model):
    name = models.CharField('Name', max_length=50)
    categoryCoupon = models.ForeignKey(CategoryCoupon, on_delete=models.CASCADE)
    vendorCoupon = models.ForeignKey(VendorCoupon, on_delete=models.CASCADE)
    description = models.TextField('Description',)
    code = models.CharField('Code', max_length=50)

    # def __str__(self):
    #     return f"{self.name}, {self.category}, {self.vendor}, {self.description}, {self.discount}, {self.price}, {self.get_sale()}"

    class Meta:
        verbose_name_plural = "Coupon"

#
class CategoryCashback(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Category Cashback"
#
#
class VendorCashback(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Vendor Cashback"


class Cashback(models.Model):
    name = models.CharField('Name', max_length=50)
    categoryCashback = models.ForeignKey(CategoryCashback, on_delete=models.CASCADE)
    vendorCashback = models.ForeignKey(VendorCashback, on_delete=models.CASCADE)
    description = models.TextField('Description',)
    ref = models.CharField('Link', max_length=50)

    class Meta:
        verbose_name_plural = "Cashback"