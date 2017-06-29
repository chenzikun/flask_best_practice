from requests.exceptions import RequestException
from flask import current_app
from json.decoder import JSONDecodeError
import requests


class JavaApiError(Exception):
    """java接口发生错误"""
    pass


def call_java_services(method, url=None, **params):
    """
    通过jsonrpc调用java接口

    :param method: 对应jsonrpc-method
    :param url: 调用链接
    :param params: 对应jsonrpc-params
    :return: json
    """
    url = url or current_app.config['CLIENT_API_URL']
    payload = dict(method=method, params=params, id=100, jsonrpc=2.0)
    try:
        resp = requests.post(url, json=payload)
    except RequestException:
        raise JavaApiError()

    try:
        return resp.json()
    except JSONDecodeError:
        raise JavaApiError()