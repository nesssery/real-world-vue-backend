# Generated by Django 3.1.3 on 2020-11-19 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20201119_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.categorie', to_field='title'),
        ),
    ]
