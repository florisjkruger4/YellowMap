# Generated by Django 4.0.5 on 2022-08-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(choices=[('Bison', 'Bison'), ('Wolf', 'Wolf'), ('Elk', 'Elk'), ('Black Bear', 'Black Bear'), ('Grizzly Bear', 'Grizzly Bear'), ('Moose', 'Moose'), ('Mountain Lion', 'Mountain Lion'), ('Coyote', 'Coyote'), ('Pronghorn', 'Pronghorn'), ('Bighorn Sheep', 'Bighorn Sheep'), ('Bald Eagle', 'Bald Eagle'), ('Bobcat', 'Bobcat'), ('Red Fox', 'Red Fox'), ('Trumpeter Swan', 'Trumpeter Swan'), ('Yellow-bellied Marmot', 'Yellow-bellied Marmot'), ('River Otter', 'River Otter'), ('Lynx', 'Lynx'), ('Shrew', 'Shrew'), ('Pika', 'Pika'), ('Squirrel', 'Squirrel'), ('Mule Deer', 'Mule Deer'), ('Sandhill Crane', 'Sandhill Crane'), ('Flying Squirrel', 'Flying Squirrel'), ('Uinta Ground Squirrel', 'Uinta Ground Squirrel'), ('Montane Vole', 'Montane Vole'), ('Eastern Meadow Vole', 'Eastern Meadow Vole'), ('Bushy-tailed Woodrat', 'Bushy-tailed Woodrat'), ('Chipmunk', 'Chipmunk'), ('Uinta Chipmunk', 'Uinta Chipmunk'), ('White-tailed Jackrabbit', 'White-tailed Jackrabbit'), ('Beaver', 'Beaver'), ('American Marten', 'American Marten'), ('Mountain Chickadee', 'Mountain Chickadee'), ('Boreal Chorus Frog', 'Boreal Chorus Frog'), ('Cutthroat Trout', 'Cutthroat Trout'), ('Great Horned Owl', 'Great Horned Owl'), ('Snowshoe Hare', 'Snowshoe Hare'), ('Rocky Mountain Elk', 'Rocky Mountain Elk'), ('Northwestern Wolf', 'Northwestern Wolf'), ('Black-footed Ferret', 'Black-footed Ferret'), ('Wolverine', 'Wolverine')], default='Bison', max_length=32)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
