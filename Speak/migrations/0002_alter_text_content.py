# Generated by Django 4.2.4 on 2023-08-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Speak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
