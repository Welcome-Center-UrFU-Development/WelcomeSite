# Generated by Django 3.1.1 on 2020-09-25 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WelcomePage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]