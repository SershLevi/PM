# Generated by Django 2.1.7 on 2019-03-11 11:37

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that user has all perms', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('birthday', models.DateField(null=True, verbose_name='birthday')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now_add=True, verbose_name='modification date')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, verbose_name='active status')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
            ],
            options={
                'verbose_name': 'accounts',
                'verbose_name_plural': 'accounts',
            },
            managers=[
                ('objects', accounts.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restriction_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='restriction id')),
                ('name', models.CharField(max_length=100)),
                ('restriction_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounts_accountgroup_restrictions', to='contenttypes.ContentType', verbose_name='restriction content type id')),
            ],
            options={
                'verbose_name': 'Account Group',
            },
        ),
    ]
