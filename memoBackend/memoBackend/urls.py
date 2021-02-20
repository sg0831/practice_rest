from django.contrib import admin
from django.urls import path, include  # 맵핑을 위한 include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("connect/", include("connect.urls") ),  # connect/로 들어오는 요청은 모두 connect/urls.py로 보내 처리하라는 의미
]
