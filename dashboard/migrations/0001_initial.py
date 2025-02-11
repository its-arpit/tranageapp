# Generated by Django 2.2.12 on 2021-06-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=500)),
                ('expiry_date', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_email', models.CharField(max_length=100)),
                ('employee_mobile', models.CharField(max_length=100)),
                ('user_type', models.CharField(default='employee', max_length=50)),
                ('assigned_project', models.CharField(max_length=100)),
                ('trip_added', models.CharField(default=0, max_length=50)),
                ('trip_verified', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mapping_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=50)),
                ('project_id', models.CharField(max_length=50)),
                ('Employee_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Add_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=500)),
                ('project_loading_location', models.CharField(max_length=1000)),
                ('project_unloading_location', models.CharField(max_length=500)),
                ('material_type', models.CharField(max_length=500)),
                ('per_trip_cost', models.CharField(max_length=500)),
                ('per_unit_cost', models.CharField(max_length=500)),
                ('project_start_date', models.CharField(max_length=500)),
                ('project_end_date', models.CharField(max_length=500)),
                ('loading_unit', models.CharField(max_length=500)),
                ('project_employee', models.CharField(max_length=50)),
                ('project_status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Active', 'Active'), ('Deactive', 'Deactive')], max_length=50)),
                ('project_discription', models.TextField()),
                ('mapped_vehicle', models.ManyToManyField(related_name='my_vehicle', to='api.VehicleRegistraionModel')),
            ],
        ),
    ]
