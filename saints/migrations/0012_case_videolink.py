# Generated by Django 3.2.9 on 2021-11-29 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saints', '0011_gateoneimage_caserel'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='videoLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]