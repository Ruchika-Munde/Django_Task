# Generated by Django 2.2.7 on 2019-12-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summaryimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagename', models.CharField(max_length=30)),
                ('Image', models.ImageField(upload_to='images/')),
                ('summary', models.TextField()),
            ],
        ),
    ]
