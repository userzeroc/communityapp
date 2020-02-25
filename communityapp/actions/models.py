from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Action(models.Model):
    # 用外键指定谁的活动
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE,
                             verbose_name='用户')
    # 活动名称
    verb = models.CharField(max_length=255,
                            verbose_name='活动名称')
    # 一个指向ContentType的外键
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE,
                                  verbose_name='活动类型')
    # 存储关系对象主键的PositiveInt字段
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True,
                                            verbose_name='目标用户')
    # 两个关系对象的通用外键
    target = GenericForeignKey('target_ct', 'target_id')

    # 活动发生的时间
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True,
                                   verbose_name='发生时间')

    class Meta:
        ordering = ('-created',)
