# Generated by Django 3.0.7 on 2020-08-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='eCoins',
            field=models.DecimalField(decimal_places=2, default=150000, max_digits=9),
        ),
    ]
