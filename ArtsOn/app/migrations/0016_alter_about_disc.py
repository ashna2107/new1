# Generated by Django 4.2.7 on 2023-12-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_about_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='disc',
            field=models.TextField(null=True),
        ),
    ]
