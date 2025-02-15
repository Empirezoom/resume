# Generated by Django 5.1.2 on 2024-10-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0022_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=180)),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now=True)),
                ('read', models.BooleanField(default=False)),
                ('not_read', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
                'managed': True,
            },
        ),
    ]
