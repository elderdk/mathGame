# Generated by Django 3.1 on 2020-09-12 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0009_chore_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='image',
            field=models.ImageField(default='chore_images/cat.png', upload_to='chore_images'),
        ),
    ]
