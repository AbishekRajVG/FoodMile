# Generated by Django 5.0.4 on 2024-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmileblog', '0009_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
