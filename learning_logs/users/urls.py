from django.urls import path, include
from.import views
app_name = 'users'
urlpatterns = [
    #身份验证
    path('', include('django.contrib.auth.urls')),
    #注册页面
    path('register/', views.register, name='register'),
]