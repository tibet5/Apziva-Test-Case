# Generated by Django 3.2.10 on 2021-12-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=254)),
                ('e_mail', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('location', models.TextField(blank=True)),
                ('hirable', models.BooleanField(null=True)),
                ('user_url', models.URLField(max_length=2000)),
                ('avatar_url', models.URLField(max_length=2000)),
            ],
        ),
    ]