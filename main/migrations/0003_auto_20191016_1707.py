# Generated by Django 2.2.6 on 2019-10-16 14:07

from django.db import migrations
import main.user


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191016_1703'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='caretaker',
            managers=[
                ('objects', main.user.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='child',
            managers=[
                ('objects', main.user.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', main.user.UserManager()),
            ],
        ),
    ]