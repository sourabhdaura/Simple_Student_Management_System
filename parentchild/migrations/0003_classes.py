# Generated by Django 4.0.6 on 2022-10-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parentchild', '0002_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
            ],
        ),
    ]
