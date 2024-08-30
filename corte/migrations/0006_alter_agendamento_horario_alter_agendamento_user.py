# Generated by Django 5.1 on 2024-08-30 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corte', '0005_agendamento_modelo_corte_alter_horario_horario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='corte.horario'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
