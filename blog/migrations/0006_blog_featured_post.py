# Generated by Django 5.0.7 on 2024-07-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_post',
            field=models.BooleanField(default=False),
        ),
    ]