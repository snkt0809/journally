# Generated by Django 5.2.1 on 2025-05-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
    ]
