# Generated by Django 3.2.9 on 2021-11-22 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountabilityGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('washingOfmaterials', 'Washing Of Materials'), ('evangelism', 'Evangelism'), ('other', 'Other Activities')], default='other', max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='reports/images')),
                ('date', models.DateField(verbose_name='')),
                ('Time', models.TimeField(null=True)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='reports/images')),
                ('location', models.CharField(max_length=20, null=True)),
                ('date', models.DateField(verbose_name='')),
                ('Time', models.TimeField(null=True)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeAltar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Senior_Pastor', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('region', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('contact', models.CharField(max_length=15)),
                ('interestedDepartment', models.CharField(choices=[('worship', 'worship'), ('ushering', 'ushering'), ('violin', 'violin'), ('keyboard', 'keyboard'), ('decoration', 'decoration'), ('hospitality', 'hospitality'), ('security', 'security')], max_length=20)),
                ('fellowship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saints.fellowship')),
                ('home_altar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='saints.homealtar')),
            ],
        ),
        migrations.CreateModel(
            name='Sunday_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('banner', models.ImageField(upload_to='services/banners')),
                ('report', models.FileField(upload_to='services/reports')),
                ('visitors', models.ManyToManyField(to='saints.Visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Saint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('residence', models.CharField(max_length=50)),
                ('stability', models.CharField(choices=[('stable', 'stable'), ('mid-stable', 'mid-stable'), ('unstable', 'unstable'), ('unresponsive', 'unresponsive')], default='unstable', max_length=15)),
                ('gender', models.CharField(choices=[('sister', 'sister'), ('brother', 'brother')], default='brother', max_length=10)),
                ('year', models.CharField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth'), ('GR', 'graduate'), ('PR', 'professional')], default='1', max_length=2)),
                ('comment', models.TextField(blank=True, null=True)),
                ('saint_level', models.CharField(choices=[('new', 'New  beleiver'), ('faithful', 'Faihful'), ('leader', 'Leader'), ('pastor', 'Pastor'), ('seniorpastor', 'Senior Pastor'), ('reverend', 'Reverend'), ('bishop', 'Bishop')], default='faithful', max_length=13)),
                ('married', models.BooleanField()),
                ('child', models.BooleanField()),
                ('accountability_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='saints.accountabilitygroup')),
                ('departments', models.ManyToManyField(to='saints.Department')),
                ('home_altar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saints.homealtar')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('report', models.TextField()),
                ('document', models.FileField(blank=True, upload_to='reports/docs')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.saint')),
                ('fellowshipA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saints.fellowship', verbose_name='fellowship')),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.saint')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='saints.activity')),
                ('fellowship', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='saints.fellowship')),
                ('saint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.saint')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='reports/images')),
                ('note', models.CharField(max_length=50)),
                ('eventType', models.CharField(choices=[('fellowship', 'Fellowship'), ('activity', 'Activity'), ('service', 'Service')], max_length=30)),
                ('Activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saints.activity', verbose_name='activity')),
                ('Service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saints.sunday_service', verbose_name='service')),
                ('fellowshipA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saints.fellowship', verbose_name='fellowship')),
            ],
        ),
        migrations.CreateModel(
            name='AccountabilityLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountability_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.accountabilitygroup')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saints.saint')),
            ],
        ),
        migrations.AddField(
            model_name='accountabilitygroup',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saints.saint'),
        ),
    ]
