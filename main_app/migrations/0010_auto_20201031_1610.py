# Generated by Django 3.1.2 on 2020-10-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20201031_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='adress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='how_to_order',
            field=models.TextField(blank=True, null=True),
        ),
    ]
