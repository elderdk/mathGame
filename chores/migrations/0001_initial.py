# Generated by Django 3.0 on 2020-01-12 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('score', models.IntegerField()),
                ('duration', models.DurationField()),
                ('description', models.CharField(max_length=1000)),
                ('done_last', models.DateTimeField(auto_now=True)),
                ('user_assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_assign', to=settings.AUTH_USER_MODEL)),
                ('user_did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_did', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
