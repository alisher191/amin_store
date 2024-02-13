# Generated by Django 5.0.2 on 2024-02-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0008_accessoriescategory_remove_computer_ssd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessoriescategory',
            name='price',
        ),
        migrations.AddField(
            model_name='accessory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='accessoriescategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название марки'),
        ),
    ]
