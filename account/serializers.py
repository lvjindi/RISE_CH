from rest_framework import serializers

from account.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=6)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "user_category", "real_name", "role_type", "create_time"]


class EditUserChSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(min_length=6, allow_blank=True, required=False, default=None)
    email = serializers.EmailField(max_length=64)
    role_type = serializers.ChoiceField(choices=User.RoleType)
    user_category = serializers.ChoiceField(choices=User.UserCategory)


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(min_length=6)
    email = serializers.EmailField(max_length=64)
    user_category = serializers.ChoiceField(choices=User.UserCategory)


class ChangeUserRoleSerializer(serializers.Serializer):
    role_type = serializers.ChoiceField(choices=User.RoleType)
