# Generated by Django 3.2.23 on 2023-12-12 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20231208_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='image',
            new_name='recipe_image',
        ),
    ]