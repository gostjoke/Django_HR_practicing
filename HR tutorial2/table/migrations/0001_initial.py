# Generated by Django 4.1.3 on 2023-03-22 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="department",
            fields=[
                (
                    "department_name",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("department_information", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="employee",
            fields=[
                (
                    "emp_id",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "department_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="table.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="vaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vaction_start", models.DateField()),
                ("vaction_end", models.DateField()),
                ("vaction_length", models.DurationField(db_column="date")),
                (
                    "emp_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="table.employee"
                    ),
                ),
            ],
        ),
    ]
