# Generated by Django 2.2.5 on 2019-09-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0010_auto_20190916_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dname_indexname',
            name='calculated_value',
            field=models.CharField(max_length=32),
        ),
    ]
