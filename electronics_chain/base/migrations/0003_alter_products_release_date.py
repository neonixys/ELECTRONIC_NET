# Generated by Django 4.2.1 on 2023-05-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок'),
        ),
    ]