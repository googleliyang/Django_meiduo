from django.db import models


# Create your models here.

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
