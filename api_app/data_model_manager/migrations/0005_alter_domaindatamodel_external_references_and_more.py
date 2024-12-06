# Generated by Django 4.2.16 on 2024-12-06 09:28

import api_app.data_model_manager.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager', '0004_alter_domaindatamodel_evaluation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaindatamodel',
            name='external_references',
            field=api_app.data_model_manager.fields.SetField(base_field=models.URLField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='domaindatamodel',
            name='related_threats',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='domaindatamodel',
            name='resolutions',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='domaindatamodel',
            name='tags',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='filedatamodel',
            name='comments',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='filedatamodel',
            name='external_references',
            field=api_app.data_model_manager.fields.SetField(base_field=models.URLField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='filedatamodel',
            name='related_threats',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='filedatamodel',
            name='tags',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='external_references',
            field=api_app.data_model_manager.fields.SetField(base_field=models.URLField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='related_threats',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='resolutions',
            field=api_app.data_model_manager.fields.SetField(base_field=models.URLField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='tags',
            field=api_app.data_model_manager.fields.SetField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
    ]
