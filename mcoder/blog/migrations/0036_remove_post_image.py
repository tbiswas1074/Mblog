# Generated by Django 4.1.2 on 2022-11-23 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
