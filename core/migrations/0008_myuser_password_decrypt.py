# Generated by Django 2.0.2 on 2019-07-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_myuser_tarjeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password_decrypt',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Contraseña'),
        ),
    ]