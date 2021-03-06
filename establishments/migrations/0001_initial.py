# Generated by Django 2.2.2 on 2019-06-24 20:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('logo', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Establishment',
                'verbose_name_plural': 'Establishments',
            },
        ),
    ]
