from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
import simplejson
from .models import User
from django.conf import settings
import bcrypt
import jwt
import datetime

AUTH_EXPIRE = 8 * 60 * 60

def get_token(user_id):
    """生成token"""
    return jwt.encode({
        'user_id':user_id,
        'exp': int(datetime.datetime.now().timestamp()) + AUTH_EXPIRE#要取整
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


def login(request:HttpRequest):
    payload = simplejson.loads(request.body)
    try:
        email = payload['email']
        user = User.objects.filter(email=email).get()

        if bcrypt.checkpw(payload['password'].encode(), user.password.encode()):
            token = get_token(user.id)
            print(token)
            res = JsonResponse({
                'user':{
                    'user_id':user.id,
                    'name': user.name,
                    'email': user.email
                }, 'token':token
            })
            res.set_cookie('Jwt', token)#演示如何set cookie
            return res
        else:
            return HttpResponseBadRequest()

    except Exception as e:
        print(e)
        return HttpResponseBadRequest()

def authenticate(view):
    def wapper(request:HttpRequest):
        paylaod = request.META.get('HTTP_JWT')
        if not paylaod:
            return HttpResponse(status=401)
        try:
            paylaod = jwt.decode(paylaod, settings.SECRET_KEY, algorithms=['HS256'])
            print(paylaod)

        except:
            return HttpResponse(status=401)

        try:
            user_id = paylaod.get('user_id, -1')
            user = User.objects.filter(pk=user_id).get()
            request.user = user
            print('-'*30)
        except Exception as e:
            print(e)
            return HttpResponse(status=401)

        ret = view(request)
        return ret
    return wapper

@authenticate
def test(request:HttpRequest):
    return HttpResponse('test')

#jwt 过期问题


