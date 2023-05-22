# Generated by Django 4.2.1 on 2023-05-22 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_alter_products_release_date'),
        ('factory', '0002_alter_factorystore_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('contactmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.contactmodel')),
                ('credit', models.IntegerField(verbose_name='Задолженность')),
                ('products', models.ManyToManyField(to='base.products', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.factorystore', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Предприниматель',
                'verbose_name_plural': 'Предприниматели',
                'ordering': ['created'],
            },
            bases=('base.contactmodel',),
        ),
    ]
