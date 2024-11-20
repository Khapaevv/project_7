# Generated by Django 5.1.3 on 2024-11-19 10:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Weekday",
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
                ("day", models.CharField(max_length=20, verbose_name="День недели")),
                (
                    "number",
                    models.IntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(7),
                        ],
                        verbose_name="Порядковый номер дня в неделе",
                    ),
                ),
            ],
            options={
                "verbose_name": ("День недели",),
                "verbose_name_plural": "Дни недели",
            },
        ),
        migrations.CreateModel(
            name="Habit",
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
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                ("location", models.CharField(max_length=255, verbose_name="Место")),
                ("time", models.TimeField(verbose_name="Время выполнения")),
                (
                    "pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(verbose_name="Время на выполнение"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец привычки",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="related_to",
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "weekdays",
                    models.ManyToManyField(
                        default=1,
                        related_name="habits",
                        to="habits.weekday",
                        verbose_name="Дни недели",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Привычка",),
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
