# Generated by Django 2.2.4 on 2020-05-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cencal', '0003_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.TextField(default='#0000ff', verbose_name='color'),
            preserve_default=False,
        ),
    ]