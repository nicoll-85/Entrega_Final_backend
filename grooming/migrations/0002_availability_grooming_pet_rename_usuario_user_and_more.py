# Generated by Django 4.1 on 2024-06-12 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("grooming", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Availability",
            fields=[
                (
                    "availability_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("date", models.DateField()),
                ("hour_start", models.IntegerField()),
                ("hour_end", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Grooming",
            fields=[
                ("grooming_id", models.AutoField(primary_key=True, serialize=False)),
                ("grooming_name", models.CharField(max_length=150)),
                ("duration", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
            fields=[
                ("pet_id", models.AutoField(primary_key=True, serialize=False)),
                ("pet_name", models.CharField(max_length=150)),
                ("pet_type", models.CharField(max_length=150)),
                ("pet_age", models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Usuario",
            new_name="User",
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("schedule_id", models.AutoField(primary_key=True, serialize=False)),
                ("available_dates", models.DateField()),
                ("available_hours", models.IntegerField()),
                (
                    "availability_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grooming.availability",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("reservation_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("hours", models.IntegerField()),
                (
                    "grooming_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grooming.grooming",
                    ),
                ),
                (
                    "pet_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grooming.pet"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="grooming.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pet",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="grooming.user"
            ),
        ),
    ]
