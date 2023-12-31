# Generated by Django 3.2.19 on 2023-09-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
            ],
            options={
                'unique_together': {('city', 'weather')},
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'unique_together': {('title', 'source')},
            },
        ),
    ]
