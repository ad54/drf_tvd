# Generated by Django 3.2.4 on 2021-06-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttest',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
