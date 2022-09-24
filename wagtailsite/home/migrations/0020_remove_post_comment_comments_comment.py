# Generated by Django 4.1.1 on 2022-09-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_rename_post_comments_related_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(default=1000, max_length=255),
            preserve_default=False,
        ),
    ]