# Generated by Django 3.1.6 on 2021-10-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211014_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]