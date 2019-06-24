# Generated by Django 2.2.2 on 2019-06-24 20:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('photo', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('opening', models.TimeField()),
                ('closing', models.TimeField()),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishments.Establishment')),
            ],
            options={
                'verbose_name': 'Stadium',
                'verbose_name_plural': 'Stadiums',
            },
        ),
    ]
