# Generated by Django 5.0 on 2024-01-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinlib', '0002_alter_image_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]
