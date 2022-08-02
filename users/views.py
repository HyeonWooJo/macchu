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