# Generated by Django 3.2.8 on 2022-03-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0011_alter_post_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(max_length=500),
        ),
    ]
