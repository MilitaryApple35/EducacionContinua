# Generated by Django 4.2.1 on 2023-06-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='cajas/')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
