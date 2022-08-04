from django.urls import path

from .views import KakaoSigninView, UserView, ProductLikeView, ProductReviewView

urlpatterns = [
    path('kakaologin', KakaoSigninView.as_view()),
    path('', UserView.as_view()),
    path('product/like', ProductLikeView.as_view()),
    path('product/review/<int:product_id>', ProductReviewView.as_view()),
]