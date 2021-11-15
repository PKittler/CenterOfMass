# Generated by Django 3.2.9 on 2021-11-12 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('label_x_min', models.CharField(max_length=30)),
                ('label_x_max', models.CharField(max_length=30)),
                ('label_y_min', models.CharField(max_length=30)),
                ('label_y_max', models.CharField(max_length=30)),
                ('label_z_min', models.CharField(max_length=30)),
                ('label_z_max', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Masspoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('x_value', models.IntegerField(default=0)),
                ('y_value', models.IntegerField(default=0)),
                ('z_value', models.IntegerField(default=0)),
                ('mass', models.FloatField(default=0)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_manager.case')),
            ],
        ),
    ]
