# Generated by Django 3.0.6 on 2020-06-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200612_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='how',
            field=models.CharField(default='delivery', max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='special_instruction',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='not_placed', max_length=200),
        ),
    ]
