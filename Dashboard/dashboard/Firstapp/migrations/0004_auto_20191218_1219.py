# Generated by Django 2.2.7 on 2019-12-18 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0003_auto_20191218_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='civiljobs',
            old_name='user_it',
            new_name='user_civil',
        ),
        migrations.RenameField(
            model_name='mechjobs',
            old_name='user_it',
            new_name='user_mech',
        ),
    ]