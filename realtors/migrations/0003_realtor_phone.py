# Generated by Django 3.2.4 on 2021-07-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='phone',
            field=models.CharField(default='555-555-5555', max_length=20),
        ),
    ]