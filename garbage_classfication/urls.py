"""garbage_classfication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # index下的网址都由index下的urls控制
    path('index/', include('index.urls')),
    # 传入时namespace 和 app_name 必须要有一个 app_name可以设置在app.urls下
    # namespace不是必须的,但在指定namespace时无app_name不允许
    # 有app_name则必须是元组参数
    path('tasks/', include(('tasks.urls', 'tasks'), namespace='tasks'))
]
