# Generated by Django 5.1.2 on 2024-10-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0006_alter_about_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='date_of_birth',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]