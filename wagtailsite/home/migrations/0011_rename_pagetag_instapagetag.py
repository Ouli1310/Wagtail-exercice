# Generated by Django 4.1.1 on 2022-09-24 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('home', '0010_pagetag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageTag',
            new_name='InstaPageTag',
        ),
    ]