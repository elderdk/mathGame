# Generated by Django 3.0 on 2020-01-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200109_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultsetting',
            name='allowedOperators',
            field=models.CharField(default='+', max_length=15),
        ),
    ]
