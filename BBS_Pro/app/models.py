from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#帖子表
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    auth = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    create_d = models.DateTimeField()
    update_d = models.DateTimeField()
    def __unicode__(self):
        return self.title

#板块表
class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')


#用户表
class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy too lazy to levave anything here')
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user-1.jpg")
    def __str__(self):
        return self.user.username