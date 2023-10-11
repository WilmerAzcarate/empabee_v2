# Generated by Django 4.2.6 on 2023-10-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'cultivo',
                'managed': True,
            },
        ),
    ]