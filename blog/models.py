from django.db import models


# Create your models here.

# 要继承models.Model类，固定写法
class UserInfo(models.Model):
    # 创建两个字段，最大长度32，类型是char
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
