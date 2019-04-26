import jwt
import base64

key = 'secret'
token = jwt.encode({'payload':'abc123'}, key, 'HS256')
print(token)
print(jwt.decode(token, key, algorithms=['HS256']))

header, payload, signature = token.split(b'.')
print(header)
print(payload)
print(signature)

def addeq(b:bytes):
    """为base64编码补齐等号
    解码是将4个字符变成三个byte"""
    rem = len(b) % 4
    return b + b'='*rem

print('header=' ,base64.urlsafe_b64decode(addeq(header)))
print('payload=' ,base64.urlsafe_b64decode(addeq(payload)))
print('signature=' ,base64.urlsafe_b64decode(addeq(signature)))

#跟进jwt算法，重新生成签名
#1获取算法对象
from jwt import algorithms
alg = algorithms.get_default_algorithms()['HS256']
newkey = alg.prepare_key(key)

#获取前两部分 header,payload
signing_input,_,_ = token.rpartition(b'.')
print(signing_input,'+!+!+!+')

#使用key签名
signature = alg.sign(signing_input, newkey)
print('--------------')
print(signature)
print(base64.urlsafe_b64encode(signature))

import json
print(base64.urlsafe_b64encode(json.dumps({'payload':'abc123'}).encode()))