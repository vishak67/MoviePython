# Generated by Django 3.2.8 on 2021-10-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='caption', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
