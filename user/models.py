from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import MinimumLengthValidator
from .validators import PasswordValidator
from django.utils.translation import gettext_lazy as _

class UserInfo(AbstractUser):
    passwordRegex = RegexValidator(regex=r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    password = models.CharField(max_length=150,
                                help_text="비밀번호는 8자리 이상이며 영문, 숫자를 1개 이상 포함해야 합니다.", 
                                validators=[passwordRegex],
                                )
    password_check = models.CharField(max_length=150, null=True, default='')                        # 비밀번호 확인
    name = models.CharField(max_length=50)                                                          # 이름
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators = [phoneNumberRegex], 
                                    max_length = 11)                                                # 전화번호(유효성 추가)
    
    def __str__(self):
        return self.username
