# Generated by Django 4.1 on 2024-06-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name_owner", models.CharField(max_length=150)),
                ("phone", models.IntegerField()),
                ("email", models.CharField(max_length=200)),
                ("id_owner", models.IntegerField()),
            ],
        ),
    ]
