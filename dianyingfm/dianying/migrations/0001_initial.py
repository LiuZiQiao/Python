# Generated by Django 2.2.6 on 2019-11-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=32)),
                ('upasswd', models.CharField(max_length=32)),
            ],
        ),
    ]