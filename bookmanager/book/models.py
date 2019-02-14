from django.db import models
from datetime import datetime


# Create your models here.


class BookInfo(models.Model):
    # todo1: pass 11 try, it's ok , what's the useful
    name = models.CharField(max_length=10)
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        """Define every data obj show"""
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    # auto generate id key as primary
    name = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    # foreign key, book belong to which book
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name



# exclude except aggregate

