# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-08 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20190106_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status_rollback',
            field=models.IntegerField(choices=[(0, '待回滚'), (1, '正在回滚'), (2, '回滚成功'), (3, '回滚失败')], default=0, verbose_name='回滚状态'),
        ),
        migrations.AddIndex(
            model_name='projectenvconfig',
            index=models.Index(fields=['project', 'env'], name='deploy_proj_project_aec5b9_idx'),
        ),
    ]