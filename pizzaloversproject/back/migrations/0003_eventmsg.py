# Generated by Django 3.1.5 on 2021-01-22 20:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20210122_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMsg',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
    ]