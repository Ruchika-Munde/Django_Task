# Generated by Django 2.2.7 on 2019-12-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Postapp', '0002_auto_20191216_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.TextField()),
                ('tagsforpost', models.ManyToManyField(to='Postapp.Post')),
            ],
        ),
    ]
