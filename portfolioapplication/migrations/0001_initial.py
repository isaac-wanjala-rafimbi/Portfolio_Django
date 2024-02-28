# Generated by Django 4.1.1 on 2024-02-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField()),
                ('about_photo', models.ImageField(upload_to='about_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_photo', models.ImageField(upload_to='project_photos/')),
                ('name', models.CharField(max_length=100)),
                ('project_link', models.URLField()),
                ('readmore_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_photo', models.ImageField(upload_to='testimonial_photos/')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('testimonial_message', models.TextField()),
                ('social_link_facebook', models.URLField(blank=True, null=True)),
                ('social_link_twitter', models.URLField(blank=True, null=True)),
                ('social_link_linkedin', models.URLField(blank=True, null=True)),
                ('social_link_instagram', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
