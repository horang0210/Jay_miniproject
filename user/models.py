from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    name = models.CharField(max_length=50)                      # 이름
    phone_number = models.CharField(max_length=50)              # 전화번호

    def __str__(self):
        return self.username


# class UserInfo(models.Model):
#     username = models.CharField(max_length=150, unique=True)    #ID
#     password = models.CharField(max_length=150)                 #password
#     name = models.CharField(max_length=50)                      #이름
#     phone_number = models.CharField(max_length=50)              #전화번호