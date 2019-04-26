from django.conf.urls import url
from .views import reg
#临时测试调用reg视图函数
from django.http import HttpResponse, HttpRequest

# def reg(request:HttpRequest):
#     return HttpResponse(b'user.reg')

urlpatterns =[
    url(r'^reg$', reg)
]