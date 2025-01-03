# Generated by Django 5.1.4 on 2024-12-26 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Containers",
            fields=[
                ("container_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "container_name",
                    models.CharField(
                        help_text="컨테이너 이름은 username과 동일하게 해주세요.",
                        max_length=150,
                        unique=True,
                    ),
                ),
                (
                    "is_created",
                    models.BooleanField(
                        default=False, help_text="컨테이너 생성을 원한다면 체크해주세요."
                    ),
                ),
                (
                    "username",
                    models.OneToOneField(
                        db_column="username",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="containers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
