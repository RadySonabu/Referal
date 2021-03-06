# Generated by Django 3.0.8 on 2021-06-03 01:57

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('modified_by', models.CharField(max_length=50)),
                ('modified_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('modified_by', models.CharField(max_length=50)),
                ('modified_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('modified_by', models.CharField(max_length=50)),
                ('modified_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referal.Category')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referal.Location')),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
    ]
