# Generated by Django 4.1.2 on 2022-11-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_like_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
