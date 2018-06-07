from django.conf.urls import url
import json
from django.http import HttpResponse
import redis
import re

def test(request):
    resp = {'wtf': 1, 'aaa': 2}
    # return HttpResponse('hello, world!')
    return HttpResponse(json.dumps(resp), content_type='application/json')


def get_keys(request):
    p = redis.Redis(host='114.212.189.147', port=10104, decode_responses=True)
    keys, ids = p.keys(), []
    for key in keys:
        ids.extend(re.findall(r'tasks_record_(.+)', key))
    return HttpResponse(json.dumps(ids), content_type='application/json')


def get_record(request, id):
    p = redis.Redis(host='114.212.189.147', port=10104, decode_responses=True)
    key = 'tasks_record_' + str(id)
    record = p.lrange(key, 0, -1)
    return HttpResponse(json.dumps(json.loads(record)), content_type='application/json')
