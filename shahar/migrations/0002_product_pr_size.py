# Generated by Django 4.2.13 on 2024-07-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pr_size',
            field=models.CharField(choices=[('m', 32), ('L', 42), ('XL', 52)], default=32, max_length=5, verbose_name='اندازه'),
        ),
    ]