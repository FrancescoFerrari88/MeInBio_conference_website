# Generated by Django 2.2.9 on 2020-01-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200111_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contribution',
            field=models.CharField(choices=[('TK', 'Talk'), ('PO', 'Poster')], default='TK', max_length=2),
        ),
    ]