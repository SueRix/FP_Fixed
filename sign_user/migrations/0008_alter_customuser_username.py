# Generated by Django 4.2.5 on 2023-11-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_user', '0007_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
