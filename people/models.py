from django.db import models


# Create your models here.

class Staff(models.Model):
    name = models.TextField()
    office = models.TextField(null=True)
    phone = models.TextField(null=True)
    email = models.TextField(null=True)
    position = models.TextField(null=True)  # 职位（中心主任，助理教授，主任助理，博士后）
    degree = models.TextField(null=True)  # 学位（本科，硕士，博士，FBCS）
    professionalTitle = models.TextField()  # 职称（教授，副教授，讲师）
    profession = models.TextField(null=True)  # 导师类型（博士导师，硕士导师）
    area = models.TextField(null=True)
    interesting = models.TextField(null=True)
    biography = models.TextField(null=True)
    project = models.TextField(null=True)
    achievement = models.TextField(null=True)
    activity = models.TextField(null=True)
    publication = models.TextField(null=True)
    report = models.TextField(null=True)
    img = models.TextField(null=True)
    imgPath = models.TextField(null=True)
    link = models.TextField(null=True)
    status = models.BooleanField(null=True)  # 状态（在职，不在职）
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_staff'


class Student(models.Model):
    name = models.TextField()
    email = models.TextField(null=True)
    enrollmentTime = models.DateTimeField(null=True)
    graduationTime = models.DateTimeField(null=True)
    type = models.TextField(null=True)  # 学生类型（硕士，博士,本科生）
    graduateStatus = models.TextField(null=True, default="在读")  # 学生状态（在读，毕业）
    supervisor = models.TextField(null=True, default="刘志明教授")  # 导师（刘志明教授，赖红副教授，叶明副教授）
    supervisorLink = models.TextField(null=True)  # 导师主页连接
    img = models.TextField(null=True)
    imgPath = models.TextField(null=True)
    project = models.TextField(null=True)
    activity = models.TextField(null=True)
    publication = models.TextField(null=True)
    area = models.TextField(null=True)
    biography = models.TextField(null=True)
    link = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_student'


class AdjunctProfessor(models.Model):
    name = models.TextField()
    email = models.TextField(null=True)
    degree = models.TextField(null=True)  # 学位（本科，硕士，博士，FBCS）
    professionalTitle = models.TextField(null=True)  # 职称（教授，副教授，讲师）
    img = models.TextField(null=True)
    imgPath = models.TextField(null=True)
    area = models.TextField(null=True)
    biography = models.TextField(null=True)
    link = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cn_rise_adjunct_professor'
