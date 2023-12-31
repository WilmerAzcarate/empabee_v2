# Generated by Django 4.2.6 on 2023-10-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piscicultura', '0003_alter_produccionestanque_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='especiepez',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='especiepez',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='estanque',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='estanque',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='produccionestanque',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='produccionestanque',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
