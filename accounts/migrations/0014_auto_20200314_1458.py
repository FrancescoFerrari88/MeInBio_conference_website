# Generated by Django 2.2.9 on 2020-03-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200314_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='expertise',
            field=models.TextField(default='', verbose_name='What are your expertise?'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='tolearn',
            field=models.TextField(default='', verbose_name='What would you still like to learn?'),
        ),
    ]
