

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [path('admin/', admin.site.urls),#定义的管理员页面链接
               path('', include('learning_log.urls')),
               path('users/', include('users.urls')),]
