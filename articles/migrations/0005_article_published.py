# Generated by Django 5.2.1 on 2025-06-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_timestamp_article_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
