from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{"{}__iexact".format(self.model.USERNAME_FIELD): username})


class User(AbstractBaseUser):
    RoleType = (
        ('Super Admin', u'超级管理员'),
        ('Regular User', u'普通用户')
    )
    UserCategory = (
        ('staff', u'职工'),
        ('student', u'学生'),
        ('adjunctProfessor', u'兼职教授'),
    )
    username = models.CharField(unique=True, max_length=64)
    email = models.TextField(null=True)
    real_name = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    user_category = models.TextField(choices=UserCategory, null=True)
    role_type = models.TextField(choices=RoleType, default='Regular User')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def is_super_admin(self):
        return self.role_type == 'Super Admin'

    class Meta:
        db_table = 'cn_rise_user'
