# Generated by Django 2.2.5 on 2019-09-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0004_auto_20190916_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(help_text='Enter field documentation', max_length=100, unique=True),
        ),
    ]