# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 11:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('juser', '0001_initial'),
        ('jasset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('results', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_finish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PermPush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public_key', models.BooleanField(default=False)),
                ('is_password', models.BooleanField(default=False)),
                ('success', models.BooleanField(default=False)),
                ('result', models.TextField(default='')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perm_push', to='jasset.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='PermRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('comment', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('password', models.CharField(max_length=512)),
                ('key_path', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PermRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('comment', models.CharField(max_length=100)),
                ('asset', models.ManyToManyField(related_name='perm_rule', to='jasset.Asset')),
                ('asset_group', models.ManyToManyField(related_name='perm_rule', to='jasset.AssetGroup')),
                ('role', models.ManyToManyField(related_name='perm_rule', to='jperm.PermRole')),
                ('user', models.ManyToManyField(related_name='perm_rule', to=settings.AUTH_USER_MODEL)),
                ('user_group', models.ManyToManyField(related_name='perm_rule', to='juser.UserGroup')),
            ],
        ),
        migrations.CreateModel(
            name='PermSudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('commands', models.TextField()),
                ('comment', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='permrole',
            name='sudo',
            field=models.ManyToManyField(related_name='perm_role', to='jperm.PermSudo'),
        ),
        migrations.AddField(
            model_name='permpush',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perm_push', to='jperm.PermRole'),
        ),
    ]
