from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # 修改密码
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # 注册
    path('register/', views.register, name='register'),
    # 编辑信息
    path('edit/', views.edit, name='edit'),
    # 关注操作路径
    path('user/follow/', views.user_follow, name='user_follow'),
    # 人员名单路由
    path('users/', views.user_list, name='user_list'),
    path('users/<username>', views.user_detail, name='user_detail'),


]
