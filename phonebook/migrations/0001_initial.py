# Generated by Django 4.0.2 on 2022-02-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('image', models.FileField(upload_to='avatars/')),
            ],
        ),
    ]