# Generated by Django 3.2.9 on 2021-11-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saints', '0003_alter_saint_attendedservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='GateOneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateofRecording', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='saint',
            name='accountability_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saints.accountabilitygroup'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('sister', 'sister'), ('brother', 'brother')], default='brother', max_length=12)),
                ('YearOfBirth', models.DateField()),
                ('StartOfCondition', models.DateField()),
                ('residence', models.CharField(max_length=25)),
                ('ailment', models.CharField(max_length=80, verbose_name='Sickness/Disability')),
                ('images', models.ManyToManyField(to='saints.GateOneImage')),
            ],
        ),
    ]