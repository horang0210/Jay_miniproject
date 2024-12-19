from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class UserInfo(AbstractUser):
    password_check = models.CharField(max_length=150, null=True, default='')                        # 비밀번호 확인
    name = models.CharField(max_length=50)                                                          # 이름
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators = [phoneNumberRegex], 
                                    max_length = 11)                                                # 전화번호(유효성 추가)
    
    def __str__(self):
        return self.username


# class UserInfo(models.Model):
#     username = models.CharField(max_length=150, unique=True)    #ID
#     password = models.CharField(max_length=150)                 #password
#     name = models.CharField(max_length=50)                      #이름
#     phone_number = models.CharField(max_length=50)              #전화번호