# Generated by Django 3.2.4 on 2021-06-24 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_studenttest_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('city', models.CharField(max_length=200)),
                ('num_of_books', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('publish', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=100)),
                ('book_num', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.author')),
            ],
        ),
        migrations.DeleteModel(
            name='StudentTest',
        ),
    ]
