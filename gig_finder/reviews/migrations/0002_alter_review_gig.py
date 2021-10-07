# Generated by Django 3.2.8 on 2021-10-07 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0002_rename_musician_id_gig_musician'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='gig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gigs.gig'),
            preserve_default=False,
        ),
    ]
