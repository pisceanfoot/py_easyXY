# -*- coding: utf-8 -*-

import requests
import string
import json

def request(api, data = None):
    """
        request(api: dic, data: dic)

        api = {
            "method": "POST", 
            "url": "http://localhost:10222/api/user/", 
            "parseJSON":True
        }
        data = {
            "userId": 123
        }
    """
    if(api is None):
        raise Exception('api can not be not or empty')

    headers = api.get('headers')
    url = __route(api, data)

    method = api.get('method', 'GET')
    if(method == 'GET'):
        return __get(api, url, data, headers)

    requestFunc = __buildRequest(method)
    return __sendRequest(requestFunc, api, url, data, headers)


def __get(api, url, data, headers):
    r = requests.get(url, params = data, headers = headers)
    return __result(api, r)


def __sendRequest(requestFunc, api, url, data, headers):
    if(api.get('json')):
        if headers:
            headers["Content-Type"] = "application/json"
        else:
            headers = {"Content-Type": "application/json"}
        r = requestFunc(url, data=json.dumps(data), headers = headers)
    else:
        r = requestFunc(url, data = data, headers = headers)

    return __result(api, r)

def __buildRequest(method):
    requestFunc = None

    if(method == 'POST'):
        requestFunc = requests.post
    elif(method == 'PUT'):
        requestFunc = requests.put
    elif(method == 'DELETE'):
        requestFunc = requests.delete
    else:
        raise Exception('method %s not support currently', method)

    return requestFunc


def __result(api, r):
    if(api.get('parseJSON')):
        return __json(r)
    else:
        return __text(r)

def __json(r):
    try:
        return r.json()
    except Exception as ex:
        raise Exception("parse json failed", __text(r), ex)

def __text(r):
    try:
        return r.text
    except Exception as ex:
        raise ex

def __route(api, data):
    url = api["url"];
    route = api.get('route')
    if(route):
        for key in route:
            tmp = data.get(key)
            url = string.replace(url, "{{{0}}}".format(key), str(tmp))
            del data[key]

    return url

if(__name__ == "__main__"):
    conf = {"method": "DELETE", "url": "http://www.baidu.com", "json": True}
    result = request(conf, {"userId":"8241f928-06dc-4061-bdf2-df12233107cd", "productTypeId": "aab1a3f3-fb46-41da-8a6d-326f09c0a79c"})
    print result