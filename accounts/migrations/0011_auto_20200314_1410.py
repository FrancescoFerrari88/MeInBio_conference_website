# Generated by Django 2.2.9 on 2020-03-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200111_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contribution',
            field=models.CharField(choices=[('TK', 'Talk'), ('IT', 'Invited Talk'), ('PO', 'Poster')], default='TK', max_length=2),
        ),
    ]
