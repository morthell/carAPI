# Generated by Django 3.2.9 on 2021-11-23 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_rating_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_avg_rating', to='api.car'),
        ),
    ]
