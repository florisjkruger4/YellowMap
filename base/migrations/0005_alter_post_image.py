# Generated by Django 4.0.5 on 2022-08-13 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/images/IMG_2057_2_copy.jpg', null=True, upload_to='images'),
        ),
    ]
