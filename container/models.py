from django.db import models
from user.models import UserInfo

# Create your models here.
class Containers(models.Model):
    container_id = models.AutoField(primary_key=True)               # container_id 자동 생성(pk)
    username = models.OneToOneField(UserInfo, 
                                 related_name="containers", 
                                 on_delete=models.CASCADE,
                                 db_column="username")          # username (fk)
    container_name = models.CharField(max_length=150,
                                      help_text="컨테이너 이름은 username과 동일하게 해주세요.",
                                      unique=True)                  # container 이름
    is_created = models.BooleanField(default=False, 
                                     null=False,
                                     help_text="컨테이너 생성을 원한다면 체크해주세요.")   # container 유무
    
    def __str__(self):
        return f"{self.username.username} - {self.container_name}"