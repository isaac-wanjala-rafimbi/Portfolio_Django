# Generated by Django 4.1.1 on 2024-03-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapplication', '0002_contact_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]