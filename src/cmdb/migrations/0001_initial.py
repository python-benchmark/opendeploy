# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ipaddr', models.CharField(max_length=64, unique=True, verbose_name='IP地址')),
                ('hostname', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='主机名')),
                ('root_password', models.CharField(blank=True, max_length=255, null=True, verbose_name='root密码')),
                ('provider', models.CharField(choices=[('own_idc', '自有IDC'), ('aliyun', '阿里云'), ('qcloud', '腾讯云')], default='own_idc', max_length=16, verbose_name='服务商')),
                ('instance_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='InstanceId')),
                ('comment', models.CharField(default='', max_length=255, verbose_name='备注')),
                ('status', models.CharField(choices=[('1', '启用'), ('0', '禁用')], default='1', max_length=2)),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
                'db_table': 'cmdb_host',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('comment', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('status', models.CharField(choices=[('1', '启用'), ('0', '禁用')], default='1', max_length=2)),
                ('host', models.ManyToManyField(to='cmdb.Host')),
            ],
            options={
                'verbose_name': '主机组',
                'verbose_name_plural': '主机组',
                'db_table': 'cmdb_group',
            },
        ),
    ]
