# Generated by Django 2.2.13 on 2020-08-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_cv_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='education',
            field=models.TextField(blank=True, default=''),
        ),
    ]