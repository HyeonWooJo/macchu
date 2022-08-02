from products.models import Product

from django.db.models import Count
from django.http      import JsonResponse
from django.views     import View

class ProductListView(View):
    def get(self, request):
            try:
                order_keyword = request.GET.get('order', None)
                order_prefixes = {
                    'likes' :'-like_count', 
                    #'recent':'-end_datetime', 
                    'random':'?'
                }
                order    = order_prefixes.get(order_keyword, 'id')
                products = Product.objects.annotate(like_count=Count('like__id'))\
                        .order_by(order)

                results = [{
                    "product_id"    : product.id,
                    "name"          : product.name,
                    "like_count"    : product.like_count,
                    "scent"         : product.scent,
                    "alchol_level"  : product.alchol_level,
                    "al_category"   : product.al_category,
                    "mb_category"   : product.mb_category,
                    "images"        : [url for url in product.images.url]
                }for product in products]

                return JsonResponse({'results' : results}, status = 200)
            except KeyError:
                return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
            except Product.DoesNotExist:
                return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'}, status = 400)