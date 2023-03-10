# Generated by Django 4.0 on 2022-02-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "officialapi",
            "0004_accessories_complaint_remove_badminton_reported_date_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="cycle",
            old_name="recieved_date",
            new_name="service_attended_date",
        ),
        migrations.AddField(
            model_name="cycle",
            name="remarks",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="badminton",
            name="remarks",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
