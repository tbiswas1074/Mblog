# Generated by Django 4.1.2 on 2022-11-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_thumbsup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thubsup',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('thumb', models.IntegerField(default=0)),
            ],
        ),
    ]
