from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from rest_framework.exceptions import ValidationError

from account.decorators import login_required, super_admin_required
from account.models import User
from account.serializers import UserLoginSerializer, UserChangePasswordSerializer, UserRegisterSerializer, \
    ChangeUserRoleSerializer, UserSerializer
from utils.api.api import validate_serializer, APIView


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
                # request.session['auth_user_id']
                # if auth.authenticate(username=username, password=password):
                #     print("chenggong ")
                # else:
                #     print("shibai")
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
                                       user_category=data['user_category'])
            user.set_password(password)
            user.save()
            return self.success("Succeeded")
        except ValidationError as e:
            return self.error("create user wrong")


class UserChangeRoleAPI(APIView):
    # @validate_serializer(ChangeUserRoleSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        user = auth.authenticate(username=request.user.username, password=data['password'])
        if user:
            user.role_type = data['role_type']
            user.save()
            return self.success("Succeeded")

    @super_admin_required
    def get(self, request):
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                return self.success(UserSerializer(user).data)
            except User.DoesNotExist:
                return self.error("User does not exist")
        else:
            user = User.objects.all()
            return self.success(self.paginate_data(request.user, UserSerializer))
