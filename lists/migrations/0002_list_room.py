# Generated by Django 2.2.5 on 2020-09-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='room',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Room'),
        ),
    ]
