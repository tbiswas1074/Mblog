# Generated by Django 4.1.2 on 2022-11-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_blogcomment_dislike_remove_blogcomment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/img/i.jpg', upload_to='static/img'),
        ),
    ]
