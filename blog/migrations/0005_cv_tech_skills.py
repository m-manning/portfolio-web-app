# Generated by Django 2.2.13 on 2020-08-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200830_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='tech_skills',
            field=models.TextField(blank=True, default=''),
        ),
    ]