# Generated by Django 2.2.4 on 2020-02-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Systemmanage', '0002_globalparameter_p_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparameter',
            name='p_instruction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]