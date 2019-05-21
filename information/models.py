from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Type(models.Model):
    name = models.CharField(verbose_name="类别名称", max_length=20)


class File(models.Model):
    file = models.FileField(
        verbose_name="文件"
    )


class Image(models.Model):
    image = models.ImageField(
        verbose_name="图片"
    )


class Information(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="发表用户",
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Type,
        verbose_name="文章类别",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name="文章标题",
        max_length=256
    )
    content = models.TextField(
        verbose_name="文章内容"
    )
    file = models.ManyToManyField(
        File,
        verbose_name="上传文件"
    )
    image = models.ManyToManyField(
        Image,
        verbose_name="图片"
    )
