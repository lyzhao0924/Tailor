from django.db import models
from utils.get_hash import get_hash
from db.base_model import BaseModel
# Create your models here.

class PassportManager(models.Manager):
    def add_one_passport(self,username,password,email):
        #t添加一个账户信息
        passport = self.create(username=username,password=get_hash(password,email = email))

        return passport
    
    def get_one_passport(self,username,passworld):
        try:
            passport = self.get(username=username,passworld=Get_hash(passworld))

        except self.model.DoseNotExit:
            passport = None
        return passport



class Passport(BaseModel):
    username = models.CharField(max_length=20,unique=True,verbose_name='用户昵称')
    password = models.CharField(max_length=40,verbose_name= '用户密码')
    email = models.EmailField(verbose_name= '用户邮箱')
    is_actve= models.BooleanField(default=False,verbose_name='激活状态')

    #用户表的管理器
    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'


