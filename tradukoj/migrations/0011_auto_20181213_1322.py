# Generated by Django 2.0.4 on 2018-12-13 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradukoj', '0010_auto_20181213_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationkey',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_keys', to='tradukoj.Namespace'),
        ),
        migrations.AlterUniqueTogether(
            name='translationkey',
            unique_together={('namespace', 'text')},
        ),
    ]