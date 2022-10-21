# Generated by Django 4.1.2 on 2022-10-18 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LenguajeM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Leng', models.CharField(max_length=20)),
                ('Historia', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=300)),
                ('Año_Experiencia', models.PositiveIntegerField()),
                ('Horas', models.PositiveIntegerField()),
                ('Link_Cont', models.URLField(blank=True, null=True, verbose_name='Dirección Web')),
                ('Fecha_Creacion', models.DateTimeField(auto_now_add=True)),
                ('Creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lenguajes', to='cursosR.lenguajem')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comentario', models.CharField(max_length=200)),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='cursosR.course')),
                ('NombreU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]