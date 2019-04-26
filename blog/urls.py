"""blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse, HttpRequest,JsonResponse
from django.shortcuts import render


from django.template import loader,RequestContext
#最基础的版本
# def index(request):
#     """视图函数，请求进来响应
#     """
#     return HttpResponse(b'paltu')
#使用的JsonRequest
# def index(request):
#     """视图函数：请求进来返回响应"""
#     d= {}
#     d['method'] = request.method
#     d['path'] = request.path
#     d['path_info'] = request.path_info
#     d['GETparams'] = request.GET
#     return JsonResponse(d)
def index(request:HttpRequest):
    """视图函数，请求进来返回响应"""
    # template = loader.get_template('index.html')
    # context = (request, {'content': 'www.platu.com'})
    # print(type(context))
    # return template.render(context)
    return render(request, 'index.html', {'content': 'www.paltu.com'})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^$', index),
    url(r'^user/', include('user.urls'))
]

