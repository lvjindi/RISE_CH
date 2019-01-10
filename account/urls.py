
from django.conf.urls import url

from account.views.admin import UserLoginAPI, UserLogoutAPI, UserChangePasswordAPI, UserRegisterAPI, UserChangeRoleAPI

urlpatterns = [
    url(r"^login/?$", UserLoginAPI.as_view(), name="user_login_api"),
    url(r"^logout/?$", UserLogoutAPI.as_view(), name="user_logout_api"),
    url(r"^register/?$", UserRegisterAPI.as_view(), name="user_register_api"),
    url(r"^change_role/?$", UserChangeRoleAPI.as_view(), name="user_change_role_api"),
    url(r"^change_password/?$", UserChangePasswordAPI.as_view(), name="user_change_password_api"),

]