from django.contrib import admin
from .models import Question

# Register your models here.

# 超级用户（管理员）
# 用户名：admin     邮箱：admin@toshiba.com
# 密码：sdc123456

admin.site.register(Question)
