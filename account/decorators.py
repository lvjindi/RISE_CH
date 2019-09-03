import functools
import logging
import traceback

from django.http import HttpResponse
from rest_framework.utils import json

from utils.api.api import JSONResponse


class BasePermissionDecorator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def error(self, data):
        return JSONResponse.response({"error": "permission-denied", "data": data})

    def __call__(self, *args, **kwargs):
        self.request = args[1]
        permission = self.check_permission()
        if permission:
            return self.func(*args, **kwargs)
        else:
            return self.error("You don't have permisssion")

    def check_permission(self):
        raise NotImplementedError()


class login_required(BasePermissionDecorator):
    def check_permission(self):
        return self.request.user.is_authenticated


class super_admin_required(BasePermissionDecorator):
    def check_permission(self):
        user = self.request.user
        return user.is_authenticated and user.is_super_admin()


logger = logging.getLogger('django')


def auto_log(func):
    """
    自动记录日志的装饰器：
    :param func:
    :return:
    """

    @functools.wraps(func)
    def _deco(*args, **kwargs):
        try:
            real_func = func(*args, **kwargs)
            return real_func
        except Exception as e:
            logger.error(traceback.format_exc())
            return False, e.__str__()

    return _deco
