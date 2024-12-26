# Generated by Django 5.1.4 on 2024-12-26 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0008_alter_userinfo_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="password",
            field=models.CharField(
                help_text="비밀번호는 8자리 이상이며 영문, 숫자를 1개 이상 포함해야 합니다.",
                max_length=150,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^(?=.*[a-zA-Z])(?=.*\\d)[a-zA-Z\\d]{8,}$"
                    )
                ],
            ),
        ),
    ]