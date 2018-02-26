"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# 路由配置
# 路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。

from django.conf.urls import url
from django.contrib import admin
from blog import views      # 需要先导入对应app的views文件

urlpatterns = [
    # url(r'^admin/', admin.site.urls),         # admin后台的路由，先注释掉
    url(r'^', views.index),                       # 可以设置主页
    url(r'^index/', views.index),                 # 你的路由，重点是引号中的正则表达式和后面的业务逻辑函数
]
