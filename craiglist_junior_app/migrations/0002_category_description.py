# Generated by Django 3.2.5 on 2021-07-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craiglist_junior_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
