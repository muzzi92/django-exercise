# Generated by Django 2.1.3 on 2018-11-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
                ('table_number', models.IntegerField()),
                ('item', models.CharField(max_length=200)),
                ('complete', models.BooleanField()),
            ],
        ),
    ]