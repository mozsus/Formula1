# Generated by Django 2.2.28 on 2024-03-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
        migrations.AlterField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(null=True),
        ),
    ]
