from django.db import models

from core.models  import TimeStampModel
from users.models import Review

class Product(TimeStampModel):
    name         = models.CharField(max_length=50, null=True)
    scent        = models.CharField(max_length=50, null=True)
    alchol_level = models.CharField(max_length=50, null=True)
    price        = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    images       = models.ManyToManyField("ProductImage", through="ProductProductImage")
    tags         = models.ManyToManyField("Tag", through="ProductTag")
    review       = models.ForeignKey(Review, on_delete=models.CASCADE)
    al_category  = models.ForeignKey("AlCategory", on_delete=models.CASCADE)
    mb_category  = models.ForeignKey("MbCategory", on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    url = models.URLField(max_length=150)

    class Meta:
        db_table = 'products_images'

class Tag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name    = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'tags'

class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag     = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_tags'

class ProductProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_products_images'

class AlCategory(models.Model):
    name = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'al_categories'

class MbCategory(models.Model):
    name = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'mb_categories'