# Generated by Django 3.2.9 on 2021-11-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saints', '0005_auto_20211125_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='ailment',
            new_name='condition',
        ),
        migrations.AddField(
            model_name='case',
            name='contact',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]