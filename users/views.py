import json
import jwt

from django.views import View
from django.http  import JsonResponse
from django.conf  import settings

from core.excepts    import Kakaoerror
from core.utils      import KakaoAPI, login_decorator
from users.models    import User, ProductLike
from products.models import Product

class KakaoSigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            code = data['code']

            kakao_api = KakaoAPI(settings.KAKAO_REST_API_KEY, settings.KAKAO_REDIRECT_URI)

            kakao_token   = kakao_api.get_kakao_token(code)
            kakao_profile = kakao_api.get_kakao_profile(kakao_token)

            user, is_created = User.objects.get_or_create(
                kakao_id = kakao_profile['id'],
                defaults = {
                    'email'    : kakao_profile['kakao_account']['email'],
                    'nickname' : kakao_profile['properties']['nickname']
                }
            )

            status_code = 201 if is_created else 200

            access_token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, settings.ALGORITHM)
            return JsonResponse({'token': access_token}, status=status_code)
                
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)
        except Kakaoerror as e:
            return JsonResponse({'MESSAGE' : e.message}, status = e.status)

class UserView(View):
    @login_decorator
    def get(self, request):
        user = request.user

        result = {
            'user_id'  : user.id,
            'nickname' : user.nickname,
            'email'    : user.email
        }
        return JsonResponse({'result': result}, status=200)

class LikeView(View):  
    @login_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']
            product    = Product.objects.get(id=product_id)

            if ProductLike.objects.filter(user=user, product=product).exists():
                ProductLike.objects.filter(user=user, product=product).delete()
                like_count = ProductLike.objects.filter(product=product).count()
                return JsonResponse({'message': 'SUCCESS', 'like_count':like_count}, status=200)

            ProductLike.objects.create(
                product = product,
                user    = user
            )
            like_count = ProductLike.objects.filter(product=product).count()

            return JsonResponse({'message': 'SUCCESS', 'like_count': like_count}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({"message" : "PROJECT_DOES_NOT_EXIST"}, status=400)

    @login_decorator
    def get(self, request):
        user          = request.user
        like_products = ProductLike.objects.filter(user=user)

        like_products = [
            {
                "user_id"       : user.id,
                "product_id"    : like_product.product.id,
                "name"          : like_product.product.name,
                "scent"         : like_product.product.scent,
                "alchol_level"  : like_product.product.alchol_level,
                "al_category"   : like_product.product.al_category,
                "mb_category"   : like_product.product.mb_category,
            } for like_product in like_products
        ]

        return JsonResponse({'result' : like_products}, status=200)