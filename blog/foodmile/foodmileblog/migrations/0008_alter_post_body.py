# Generated by Django 5.0.4 on 2024-04-15 07:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmileblog', '0007_post_likes_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
