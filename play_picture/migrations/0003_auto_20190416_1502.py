# Generated by Django 2.2 on 2019-04-16 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play_picture', '0002_suggester_suggestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggester',
            old_name='mail',
            new_name='email',
        ),
    ]
