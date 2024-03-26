# Generated by Django 5.0 on 2024-03-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=300)),
                ('Author', models.CharField(max_length=300)),
                ('Publisher', models.CharField(max_length=300)),
                ('Publication_date', models.DateField()),
                ('Genre', models.CharField(max_length=200)),
                ('Pages', models.IntegerField()),
                ('Location', models.TextField(max_length=300)),
            ],
        ),
    ]