# Generated by Django 3.1.5 on 2021-01-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_eventmsg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
    ]