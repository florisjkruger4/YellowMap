# Generated by Django 4.0.5 on 2022-08-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_post_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
