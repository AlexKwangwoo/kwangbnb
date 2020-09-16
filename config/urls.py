"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from . import setting 장고는 세팅을 불러올대 이렇게 하면 안됨!!


urlpatterns = [
    path("admin/", admin.site.urls),
]

# urlpatterns 은 지정된 이름이다
if settings.DEBUG:  # 내가 컴퓨터로 서버돌릴떄만 이렇게 쓴다!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static이 경로를 가져다 주는것이다! 컨트롤 클릭해보셈
# URL은 settings.MEDIA_URL이것이고
# 이미지는 settings.MEDIA_ROOT 에서 가져온다!