from django.urls import path
from .views import *
from products.views import JoinProductAPIView, UserProductListView

app_name = 'accounts'

urlpatterns = [
    # 회원가입 관련 경로
    path("register/", RegisterAPIView.as_view(), name='register'),
    path("register/check-username/", UsernameCheckAPIView.as_view(), name='check-username'),
    path("register/check-email/", EmailCheckAPIView.as_view(), name='check-email'),

    # 인증 관련 경로 (로그인, 로그아웃, 회원정보 가져오기)
    path("auth/", AuthAPIView.as_view(), name='auth'),

    # 사용자 정보 관련 경로
    path("update/", UserRetrieveUpdateAPIView.as_view(), name='update'),
    path("change_password/", ChangePasswordAPIView.as_view(), name='change_password'),

    # 상품 관련 경로
    path("user_products/", UserProductListView.as_view(), name='user_products'),

    # 유저 회원 탈퇴
    path("delete/", UserDeleteAPIView.as_view(), name='delete'),
]