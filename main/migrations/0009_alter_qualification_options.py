# Generated by Django 4.1.7 on 2023-04-15 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfolio_demo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qualification',
            options={'ordering': ['year_from'], 'verbose_name': 'Qualification', 'verbose_name_plural': 'Qualifications'},
        ),
    ]
