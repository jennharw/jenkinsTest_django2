# Generated by Django 3.1.3 on 2022-01-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_auto_20220105_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img_url',
            field=models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/1200px-Logo_NIKE.svg.png'),
            preserve_default=False,
        ),
    ]
