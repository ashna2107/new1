# Generated by Django 4.2.7 on 2024-01-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
