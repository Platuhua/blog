from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
import simplejson
from .models import User
from django.conf import settings
import bcrypt
import jwt
import datetime

def get_token(user_id):
    """生成token"""
    return jwt.encode({
        'user_id':user_id,
        'timestamp':int(datetime.datetime.now().timestamp())#要取整
    }, settings.SECRET_KEY, 'HS256').decode()#字符串

def reg(request:HttpRequest):
    print(request.POST,'++++++++++++')
    print(request.body,'-----------')
    payload = simplejson.loads(request.body)
    try:
        email = payload['email']
        query = User.objects.filter(email=email)
        print(query)
        print(type(query), query.query)
        if query:
            return HttpResponseBadRequest

        name = payload['name']
        password = bcrypt.hashpw(payload['password'].encode(), bcrypt.gensalt())
        print(email, name, password)

        user = User()
        user.email = email
        user.name = name
        user.password = password
        try:
            user.save()
            return JsonResponse({'user':user.id})#如果正常，返回json数据
        except:
            raise
    except Exception as e:# 有任何异常，都返回
        print(e)
        return HttpResponseBadRequest()#这里返回实例，这不是异常类