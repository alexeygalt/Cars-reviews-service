# Generated by Django 5.0.2 on 2024-02-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["created_at"], name="reviews_com_created_9500f2_idx"
            ),
        ),
    ]