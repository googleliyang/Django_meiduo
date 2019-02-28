from django.db import models


# Create your models here.
from users.models import User


class Area(models.Model):
    name = models.CharField(max_length=10)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subs')
    # 1 自关联一对多, 观察书库表结构
    # 2 插省市区数据入表, 插入几条就好了
    # 3 设定url地址编写，查询结果, 无参为省，/市 /市/区

    class Meta:
        db_table = 'areas'
        verbose_name = '区域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Address(models.Model):
    """收货地址"""
    # 字段: 外键 用户，Area, 详细地址，手机号，固定电话邮箱
    detail_address = models.CharField(max_length=200, verbose_name='详细收货地址')
    mobile = models.CharField(max_length=20, verbose_name='手机号')
    username = models.CharField(max_length=20, verbose_name='用户名')
    email = models.CharField(max_length=100, verbose_name='邮箱')
    telephone = models.CharField(max_length=20, verbose_name='座机号')
    is_default = models.BooleanField(default=False, verbose_name='默认收货地址')
    # 绑定这个收货地址属于哪个用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    # 绑定这个收货地址属于哪个省市区
    area = models.ForeignKey(Area, on_delete=models.PROTECT, verbose_name='区域')

    class Meta:
        db_table = 'address'
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.detail_address
