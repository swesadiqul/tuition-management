# Generated by Django 4.0.3 on 2022-03-31 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_tuitionprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuitionprofile',
            name='education',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
