# Generated by Django 2.2.5 on 2020-09-27 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_bookedday'),
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation', to='reservations.Reservation'),
        ),
    ]