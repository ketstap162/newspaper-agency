# Generated by Django 4.1 on 2022-11-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(null=True),
        ),
    ]
