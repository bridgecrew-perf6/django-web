# Generated by Django 3.1 on 2021-11-13 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20211113_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='chain_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='first_app.chains'),
            preserve_default=False,
        ),
    ]
