# Generated by Django 3.2.23 on 2023-12-08 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('community', '0002_auto_20231201_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
    ]