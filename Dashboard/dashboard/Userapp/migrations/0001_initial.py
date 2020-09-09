# Generated by Django 2.2.7 on 2019-12-17 13:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Confirmpassword', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobileno', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('Address', models.CharField(max_length=30)),
                ('Resume', models.FileField(upload_to='FileUpload/')),
            ],
        ),
    ]