# Generated by Django 2.0.4 on 2018-05-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradukoj', '0004_auto_20180516_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationkey',
            name='namespace',
            field=models.CharField(default='global', max_length=255, verbose_name='namespace'),
        ),
    ]
