# Generated by Django 5.0.2 on 2024-02-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0011_brand_alter_computer_video_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoriescategory',
            name='model_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название модели'),
        ),
    ]
