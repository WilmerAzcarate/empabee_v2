# Generated by Django 4.2.6 on 2023-10-11 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_tiptrata_tsensor_tratamiento_sensor'),
        ('piscicultura', '0004_especiepez_created_at_especiepez_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSensorEstanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechahora', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estanque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piscicultura.estanque')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.sensor')),
            ],
            options={
                'db_table': 'm_sensor_estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InfotrataEstanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('f_inicio', models.DateField()),
                ('f_fin', models.DateField()),
                ('estanque_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piscicultura.estanque')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.tratamiento')),
            ],
            options={
                'db_table': 'infotrata_estanque',
                'managed': True,
            },
        ),
    ]
