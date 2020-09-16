# Generated by Django 2.2.5 on 2020-09-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room type'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
