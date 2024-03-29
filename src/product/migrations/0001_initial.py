# Generated by Django 3.2 on 2021-04-27 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sweetName', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='jumia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('manufacture', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField()),
                ('img', models.TextField()),
                ('url', models.TextField()),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('lastprice', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.category', verbose_name='category')),
            ],
            options={
                'db_table': 'jumia',
            },
        ),
    ]
