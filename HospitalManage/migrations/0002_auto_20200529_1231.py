# Generated by Django 3.0.5 on 2020-05-29 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='conformpass',
            new_name='conformpassword',
        ),
    ]