# Generated by Django 2.1 on 2018-08-04 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poltronas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poltrona',
            name='espetaculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espetaculos.Espetaculo'),
        ),
    ]