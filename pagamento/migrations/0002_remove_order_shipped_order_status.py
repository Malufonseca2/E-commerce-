# Generated by Django 5.0.6 on 2024-06-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipped',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], default='C', max_length=1),
        ),
    ]
