# Generated by Django 2.2.28 on 2024-03-07 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0002_auto_20240307_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
