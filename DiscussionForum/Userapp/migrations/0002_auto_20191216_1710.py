# Generated by Django 2.2.7 on 2019-12-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usename',
            new_name='username',
        ),
    ]
