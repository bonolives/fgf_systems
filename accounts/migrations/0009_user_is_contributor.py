# Generated by Django 5.0 on 2023-12-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_remove_user_is_contributor_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_contributor",
            field=models.BooleanField(default=False),
        ),
    ]
