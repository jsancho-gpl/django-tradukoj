# Generated by Django 2.0.4 on 2018-11-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradukoj', '0005_auto_20180518_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcp47',
            name='direction',
            field=models.IntegerField(choices=[(0, 'Left to Right (LTR)'), (1, 'Right to Left (RTL)')], default=0),
        ),
    ]