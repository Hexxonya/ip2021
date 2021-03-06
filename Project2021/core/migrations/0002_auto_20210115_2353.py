# Generated by Django 3.1.5 on 2021-01-15 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCashback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Category Cashback',
            },
        ),
        migrations.CreateModel(
            name='VendorCashback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Vendor Cashback',
            },
        ),
        migrations.AlterModelOptions(
            name='subcategoryproduct',
            options={'verbose_name_plural': 'Subcategory'},
        ),
        migrations.CreateModel(
            name='Cashback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('ref', models.CharField(max_length=50, verbose_name='Link')),
                ('categoryCashback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categorycashback')),
                ('vendorCashback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendorcashback')),
            ],
            options={
                'verbose_name_plural': 'Cashback',
            },
        ),
    ]
