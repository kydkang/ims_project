# Generated by Django 2.2.5 on 2019-09-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0013_dname_indexname_calculated_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dname_indexname',
            name='calculated_value',
            field=models.CharField(blank=True, editable=False, max_length=32),
        ),
    ]
