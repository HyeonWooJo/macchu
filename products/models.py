from django.db import models

from core.models  import TimeStampModel
import users

class Product(TimeStampModel):
    name         = models.CharField(max_length=50, null=True)
    scent        = models.CharField(max_length=50, null=True)
    alchol_level = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True)
    price        = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    images       = models.ManyToManyField("ProductImage", through="ProductProductImage")
    tags         = models.ManyToManyField("Tag", through="ProductTag")
    review       = models.ForeignKey("users.Review", on_delete=models.CASCADE, null=True)
    al_category  = models.CharField(max_length=50, null=True)
    mb_category  = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    url = models.URLField(max_length=150)

    class Meta:
        db_table = 'products_images'

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

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