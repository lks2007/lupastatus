# Generated by Django 3.1.6 on 2021-10-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211014_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
