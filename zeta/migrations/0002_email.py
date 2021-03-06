# Generated by Django 4.0.3 on 2022-04-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=64)),
                ('sender', models.CharField(max_length=64)),
                ('body', models.TextField()),
                ('spam', models.BooleanField(default=False)),
                ('important', models.BooleanField(default=False)),
            ],
        ),
    ]
