# Generated by Django 2.2.1 on 2019-06-18 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ocra', '0004_auto_20190604_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='entrega',
            field=models.CharField(default=django.utils.timezone.now, help_text='Nombre completo del personal que entrega', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='folio_fleje',
            field=models.CharField(blank=True, help_text='Folio del fleje', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vigilante',
            name='expediente',
            field=models.CharField(help_text='número de expediente', max_length=10),
        ),
    ]
