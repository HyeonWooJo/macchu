from django.db       import models

from products.models import Product
from core.models     import TimeStampModel

class User(models.Model):
    kakao_id = models.BigIntegerField()
    email    = models.CharField(max_length=100, null=True)
    name     = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "users"

class ProductLike(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "products_likes"

class Review(TimeStampModel):
    content = models.CharField(max_length=150, null=True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "reviews"

class ReviewLike(TimeStampModel):
    review  = models.ForeignKey(Review, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "reviews_likes"

class ProductRecommendation(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "products_recommendations"