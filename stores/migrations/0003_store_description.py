# Generated by Django 3.0.5 on 2020-04-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20200414_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
