# Generated by Django 4.1 on 2022-08-30 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScaleWatcher', '0002_rename_reading_scalewatcher_reading1a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scalewatcher',
            old_name='title1a',
            new_name='Scale',
        ),
        migrations.RenameField(
            model_name='scalewatcher',
            old_name='reading1a',
            new_name='reading',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='reading1b',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='reading2a',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='reading2b',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='title1b',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='title2a',
        ),
        migrations.RemoveField(
            model_name='scalewatcher',
            name='title2b',
        ),
    ]
