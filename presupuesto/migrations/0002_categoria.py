# Generated by Django 4.0.1 on 2022-05-01 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.proyecto')),
            ],
        ),
    ]