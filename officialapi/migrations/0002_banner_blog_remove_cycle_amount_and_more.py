# Generated by Django 4.0 on 2022-01-20 06:24

import django.db.models.deletion
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("officialapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="banner",
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
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, upload_to="bannerimage"
                    ),
                ),
                (
                    "image_ppoi",
                    versatileimagefield.fields.PPOIField(
                        default="0.5x0.5", editable=False, max_length=20
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="blog",
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
                ("date", models.DateField(auto_now_add=True)),
                ("heading", models.CharField(max_length=100)),
                ("content", models.TextField(max_length=10000)),
                (
                    "image_one",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, upload_to="blogimage"
                    ),
                ),
                (
                    "image_two",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, upload_to="blogimage"
                    ),
                ),
                (
                    "image_ppoi",
                    versatileimagefield.fields.PPOIField(
                        default="0.5x0.5", editable=False, max_length=20
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="cycle",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="cycle",
            name="used_parts",
        ),
        migrations.RemoveField(
            model_name="fitness",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="fitness",
            name="used_parts",
        ),
        migrations.AddField(
            model_name="cycle",
            name="frame_no",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cycle",
            name="service_charge",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="fitness",
            name="service_charge",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="products",
            name="best_seller",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="used_parts",
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
                ("item_code", models.CharField(max_length=50)),
                ("item_name", models.CharField(max_length=50)),
                ("amount", models.IntegerField()),
                (
                    "service_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="officialapi.service_request",
                    ),
                ),
            ],
        ),
    ]
