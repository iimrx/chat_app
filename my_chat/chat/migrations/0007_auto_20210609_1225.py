# Generated by Django 3.2.4 on 2021-06-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_value_message_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
