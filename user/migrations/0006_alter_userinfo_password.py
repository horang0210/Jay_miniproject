# Generated by Django 5.1.4 on 2024-12-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_userinfo_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="password",
            field=models.CharField(max_length=150),
        ),
    ]