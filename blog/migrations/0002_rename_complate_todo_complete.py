# Generated by Django 4.1.7 on 2023-02-20 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complate',
            new_name='complete',
        ),
    ]
