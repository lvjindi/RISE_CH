from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from rest_framework.exceptions import ValidationError

from account.decorators import login_required, super_admin_required
from account.models import User
from account.serializers import UserSerializer
from utils.api.api import APIView


class UserLoginAPI(APIView):
    def get(self, request):
        return render(request, 'login/login.html')

    # @validate_serializer(UserLoginSerializer)
    def post(self, request):
        data = request.data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/api/admin/index')
            else:
                return self.error("账户未激活")
        else:
            return self.error('Invalid username or password')


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return self.success()


class UserChangePasswordAPI(APIView):
    @login_required
    # @validate_serializer(UserChangePasswordSerializer)
    def post(self, request):
        data = request.data
        user = auth.authenticate(username=request.user.username, password=data['password'])
        if user:
            user.set_password(data["new_password"])
            user.save()
            return self.success("Succeeded")
        else:
            return self.error("Invalid old password")


class UserRegisterAPI(APIView):

    def get(self, request):
        return render(request, 'login/register.html')

    # @validate_serializer(UserRegisterSerializer)
    def post(self, request):
        """
        User register api
        """
        data = request.data
        username = data['username']
        password = data['password']
        if User.objects.filter(username=username).exists():
            return self.error("Username already exists")
        if User.objects.filter(email=data["email"]).exists():
            return self.error("Email already exists")
        try:
            user = User.objects.create(username=username, email=data['email'],
                                       user_category=data['user_category'], real_name=data['real_name'])
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/api/admin/login')
        except ValidationError as e:
            return self.error("create user wrong")


class UserChangeRoleAPI(APIView):
    # @validate_serializer(ChangeUserRoleSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
            if user:
                user.email = data['email']
                user.real_name = data['real_name']
                user.user_category = data['user_category']
                user.role_type = data['role_type']
                user.save()
                return self.success("Succeeded")
        except User.DoesNotExist:
            return self.error("User does not exist")

    @super_admin_required
    def get(self, request):
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user.user_category = user.get_user_category_display()
                user.role_type = user.get_role_type_display()
                return self.success(UserSerializer(user).data)
            except User.DoesNotExist:
                return self.error("User does not exist")
        else:
            user = User.objects.all()
            for item in user:
                item.role_type = item.get_role_type_display()
                item.user_category = item.get_user_category_display()
            return self.success(self.paginate_data(request, user, UserSerializer))

    @super_admin_required
    def delete(self, request):
        user_id = request.GET.get('id')
        if user_id:
            user = User.objects.get(id=user_id)
            user.delete()
            return self.success("Succeeded")


class CheckPermissionAPI(APIView):
    def get(self, request):
        user = self.request.user
        return self.success(user.is_authenticated and user.is_super_admin())


class CheckLoginAPI(APIView):
    def get(self, request):
        user = self.request.user
        if user.is_authenticated:
            return self.success(user.username)
        else:
            return self.error("Login required!")


class UserManagementAPI(APIView):
    def get(self, request):
        return render(request, 'UserManegement.html')
