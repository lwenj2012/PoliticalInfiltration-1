# Generated by Django 2.2.4 on 2020-02-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainevent', '0002_auto_20200206_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figure',
            name='create_at',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='figure',
            name='user_birth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
