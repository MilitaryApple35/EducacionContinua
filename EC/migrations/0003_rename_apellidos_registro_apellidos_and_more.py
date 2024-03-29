# Generated by Django 4.2.1 on 2023-06-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EC', '0002_registro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Curso',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='EstadoCivil',
            new_name='estadocivil',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Municipio',
            new_name='municipio',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Nombres',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='Procedencia',
            new_name='procedencia',
        ),
        migrations.AddField(
            model_name='registro',
            name='Carrera',
            field=models.CharField(default='', max_length=50),
        ),
    ]
