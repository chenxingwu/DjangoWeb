# Generated by Django 3.0.7 on 2020-06-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200617_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/6d9de0ea26454161b6aed26ed3e679f3'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/6d9de0ea26454161b6aed26ed3e679f3', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='a954aca550f440acb891c8216cd32026', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
