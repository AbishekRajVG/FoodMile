# Generated by Django 5.0.4 on 2024-04-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmileblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='FoodMile 2.0', max_length=255),
        ),
    ]