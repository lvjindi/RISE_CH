from django.conf.urls import url

from account.views.admin import UserLoginAPI, UserLogoutAPI, UserChangePasswordAPI, UserRegisterAPI, UserChangeRoleAPI, \
    UserManagementAPI, CheckPermissionAPI, CheckLoginAPI

urlpatterns = [
    url(r"^login/?$", UserLoginAPI.as_view(), name="user_login_api"),
    url(r"^logout/?$", UserLogoutAPI.as_view(), name="user_logout_api"),
    url(r"^register/?$", UserRegisterAPI.as_view(), name="user_register_api"),
    url(r"^change_role/?$", UserChangeRoleAPI.as_view(), name="user_change_role_api"),
    url(r"^change_password/?$", UserChangePasswordAPI.as_view(), name="user_change_password_api"),
    url(r"^userManagement/?$", UserManagementAPI.as_view(), name="user_management_api"),
    url(r"^checkAdmin/?$", CheckPermissionAPI.as_view(), name="check_permission_api"),
    url(r"^checkLogin/?$", CheckLoginAPI.as_view(), name="check_login_api"),

]
