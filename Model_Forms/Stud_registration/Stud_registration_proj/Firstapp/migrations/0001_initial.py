# Generated by Django 2.2.7 on 2019-11-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('marks', models.FloatField()),
                ('addr', models.CharField(max_length=30)),
            ],
        ),
    ]