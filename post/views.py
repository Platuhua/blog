from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from user.views import authenticate
from user.models import User
import simplejson
import datetime
from .models import Post, Content
import math

@authenticate
def pub(request:HttpRequest):
    post = Post()
    conten = Content()
    try:
        payload = simplejson.loads(request.body)
        post.title = payload['title']
        post.author = User(id = request.user.id)#注入的
        post.postdata = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8))
        )

        post.save()

        conten.content = payload['content']
        conten.post = post

        conten.save()

        return JsonResponse({
            'post_id':post.id
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest


def get(request:HttpRequest, id):#分组捕获传入
    try:
        id = int(id)
        post = Post.objects.get(pk = id)
        print(post, '-------------')
        if post:
            return JsonResponse({
                'post':{
                    'post_id':post.id,
                    'title':post.title,
                    'author':post.author.name,
                    'authod_id':post.author_id,
                    'postdate':post.postdata.timestamp(),
                    'content':post.content.content
                }
            })
    except Exception as e:
        print(e)
        return HttpResponseNotFound

def vaildate(d:dict, name:str, type_func, default, validate_func):
    try:#页码
        result = type_func(d.get(name, default))
        result = validate_func(result, default)
    except:
        result = 1
    return result

def getall(request:HttpRequest):

    page = vaildate(request.GET, 'page', int, 1, lambda x,y: x if x>0 else 1)
    size = vaildate(request.GET, 'size', int, 20, lambda  x,y: x if x > 0 and x >101 else 20)

    try:
        # 按照id倒排
        start = (page -1)*size
        posts = Post.objects.order_by('-id')
        print(posts.qurey)
        count = posts.count()
        posts = posts[start:start+size]
        return JsonResponse({
            'posts':[
                {'post_id':post.id,
                'title':post.title,
                 } for post in posts],
            'pagination':{
                'page':page,
                'size':size,
                'count':count,
                'pages':math.ceil(count/size)
            }
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()





