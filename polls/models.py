from django.db import models


# Create your models here.

# 投票应用的两个模型
# 每个模型代表数据库中一张表，现在有两张表Question和Choice
# 每个类代表数据库中一张表，每个类的实例代表数据库表中的一行数据，类中每个变量代表数据表中一列字段

class Question(models.Model):
    # question_text是数据库中的字段名
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')

    # 编写此函数，在admin后台管理中可以显示返回值
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ForeignKey定义一个外键关系，它告诉Django，每一个Choice关联到一个对应的Question（注意要将外键写在‘多’的一方）
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 编写此函数，在admin后台管理中可以显示返回值
    def __str__(self):
        return self.choice_text
