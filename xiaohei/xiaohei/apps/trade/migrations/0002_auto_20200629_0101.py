# Generated by Django 3.0.7 on 2020-06-29 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='signer_mobile',
            field=models.CharField(default='', help_text='联系电话', max_length=11, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(help_text='用户', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_infos', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]