# Generated by Django 4.2.1 on 2023-05-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'super_user',
            },
        ),
    ]
