# Generated by Django 2.1.7 on 2019-03-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('customers_pic', models.ImageField(default='image', upload_to='suppliers/')),
                ('email', models.EmailField(max_length=254)),
                ('national_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('suppliers_pic', models.ImageField(default='image', upload_to='suppliers/')),
                ('email', models.EmailField(max_length=254)),
                ('national_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('litres', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
