# Generated by Django 5.0.4 on 2024-04-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_number', models.PositiveBigIntegerField(blank=True, null=True)),
                ('arabic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('arabic_description', models.CharField(blank=True, max_length=255, null=True)),
                ('english_name', models.CharField(blank=True, max_length=255, null=True)),
                ('english_description', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
