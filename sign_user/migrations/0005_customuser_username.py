# Generated by Django 4.2.5 on 2023-11-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_user', '0004_alter_customuser_email_alter_customuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='unused_username', max_length=30, unique=True),
        ),
    ]
