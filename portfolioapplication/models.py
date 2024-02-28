from django.db import models

# Create your models here.
class About(models.Model):
    about_text = models.TextField()
    about_photo = models.ImageField(upload_to='about_photos/')

    def __str__(self):
        return "About Section"

class Project(models.Model):
    project_photo = models.ImageField(upload_to='project_photos/')
    name = models.CharField(max_length=100)
    project_link = models.URLField()
    readmore_link = models.URLField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    testimonial_photo = models.ImageField(upload_to='testimonial_photos/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    testimonial_message = models.TextField()
    social_link_facebook = models.URLField(blank=True, null=True)
    social_link_twitter = models.URLField(blank=True, null=True)
    social_link_linkedin = models.URLField(blank=True, null=True)
    social_link_instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    number = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedln = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return self.email