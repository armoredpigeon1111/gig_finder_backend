# Generated by Django 3.2.8 on 2021-10-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gig',
            old_name='musician_id',
            new_name='musician',
        ),
    ]
