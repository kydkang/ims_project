# Generated by Django 2.2.5 on 2019-09-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0008_auto_20190916_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dname_indexname',
            name='calculated_value',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='dname_indexname',
            name='data_one',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='dname_indexname',
            name='data_two',
            field=models.CharField(max_length=16),
        ),
    ]
