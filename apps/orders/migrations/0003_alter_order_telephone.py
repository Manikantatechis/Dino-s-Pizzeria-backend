# Generated by Django 3.2.4 on 2022-01-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211026_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='telephone',
            field=models.IntegerField(blank=True, db_index=True, max_length=25, null=True, verbose_name='Telephone'),
        ),
    ]
