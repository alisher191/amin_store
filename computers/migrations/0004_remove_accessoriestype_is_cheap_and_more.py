# Generated by Django 5.0.2 on 2024-02-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0003_accessoriestype_image_accessoriestype_is_cheap_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessoriestype',
            name='is_cheap',
        ),
        migrations.RemoveField(
            model_name='accessoriestype',
            name='is_gaming',
        ),
        migrations.RemoveField(
            model_name='accessoriestype',
            name='is_powerful',
        ),
        migrations.AddField(
            model_name='computer',
            name='is_cheap',
            field=models.BooleanField(default=False, verbose_name='Недорогой компьютер'),
        ),
        migrations.AddField(
            model_name='computer',
            name='is_gaming',
            field=models.BooleanField(default=False, verbose_name='Игровой компьютер'),
        ),
        migrations.AddField(
            model_name='computer',
            name='is_powerful',
            field=models.BooleanField(default=False, verbose_name='Мощный компьютер'),
        ),
    ]