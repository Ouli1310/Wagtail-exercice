# Generated by Django 4.1.1 on 2022-09-24 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_post_comment_comments_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]