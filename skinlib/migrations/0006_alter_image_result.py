# Generated by Django 5.0 on 2024-01-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skinlib', '0005_alter_image_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='result',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]