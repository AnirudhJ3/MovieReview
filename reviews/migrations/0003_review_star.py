# Generated by Django 3.0.2 on 2020-02-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200207_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
