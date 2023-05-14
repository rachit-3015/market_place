# Generated by Django 3.2.18 on 2023-03-15 19:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0002_delete_listings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.TextField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
