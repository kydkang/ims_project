# Generated by Django 2.2.5 on 2019-09-20 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter department name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter index name', max_length=100)),
                ('data_one', models.IntegerField()),
                ('data_two', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calculated_value', models.CharField(blank=True, max_length=32)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.Department')),
            ],
        ),
    ]
