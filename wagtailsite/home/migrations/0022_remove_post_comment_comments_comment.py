# Generated by Django 4.1.1 on 2022-09-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_comments_comment_post_comment'),
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