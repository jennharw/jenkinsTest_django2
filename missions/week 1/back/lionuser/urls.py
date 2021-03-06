from .views import LionUserAPI, LionLoginUser, RegisterUser,LoginUser, loginTest, register, login,KakaoSignInView,kakaoTest, checkJwt

from django.urls import path

urlpatterns = [
    #회원가입 페이지
    path('register', register, name="register_page"),
    #로그인 페이지
    path('login', login, name="register_page"),

    path('login/test', loginTest, name="login_test"),
    path('login/kakao', kakaoTest, name="kakao_test"),

    path('lionregister', RegisterUser.as_view()),
    path('lionlogin', LoginUser.as_view()),

    path('lion', LionUserAPI.as_view()),  # create 회원가입
    path('lioncustomlogin', LionLoginUser.as_view()),

    path('kakao', KakaoSignInView.as_view()),
    path('check', checkJwt , name="check_jwt")

]