# Generated by Django 5.0.2 on 2024-02-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar_user_bio_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('idr', 'IDR')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('id', 'Indonesia')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
    ]
