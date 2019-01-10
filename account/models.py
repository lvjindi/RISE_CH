from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserCategory(object):
    Staff = 'Staff'
    Adjunct_Professors = 'Adjunct Professors'
    Postgraduate_Students = 'Postgraduate Student'
    Undergraduates = 'Undergraduates'


class RoleType(object):
    ADMIN = 'Admin'
    REGULAR_USER = 'Regular User'
    SUPER_ADMIN = 'Super Admin'


class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class User(AbstractBaseUser):
    username = models.CharField(unique=True,max_length=64)
    email = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    user_category = models.TextField(null=True)
    role_type = models.TextField(default=RoleType.REGULAR_USER)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def is_admin(self):
        return self.role_type == RoleType.ADMIN

    def is_super_admin(self):
        return self.role_type == RoleType.SUPER_ADMIN

    class Meta:
        db_table = 'cn_rise_user'
