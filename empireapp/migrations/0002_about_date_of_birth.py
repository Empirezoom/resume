# Generated by Django 5.1.2 on 2024-10-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='date_of_birth',
            field=models.DateField(auto_now=True),
        ),
    ]
