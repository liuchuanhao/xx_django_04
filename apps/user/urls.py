from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [


    url(r'^register$', RegisterView.as_view(), name='register'), # 注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'), # 用户激活

    url(r'^login$', LoginView.as_view(), name='login'), # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'), # 注销登录


]