# Generated by Django 2.2.4 on 2019-08-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_url', models.CharField(max_length=5000)),
                ('h3', models.CharField(max_length=5000)),
                ('h2', models.CharField(max_length=5000)),
            ],
        ),
    ]