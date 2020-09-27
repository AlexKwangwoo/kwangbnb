# Generated by Django 2.2.5 on 2020-09-27 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0003_auto_20200927_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='room',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='rooms.Room'),
        ),
    ]