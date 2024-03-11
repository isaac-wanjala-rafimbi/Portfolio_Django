from django.db import models

# Create your models here.
class About(models.Model):
    about_text = models.TextField()
    about_photo = models.ImageField(null=True, blank=True, default='default.jpg')
    resume = models.FileField(null=True, blank=True)

    def __str__(self):
        return "About Section"
    
    def imageURL(self):
        try:
            img=self.about_photo.url
        except:
            img=''
        return img

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Project(models.Model):
    project_photo = models.ImageField(null=True, blank=True, default='default.jpg')
    name = models.CharField(max_length=100)
    project_link = models.URLField()
    readmore_link = models.URLField()
    description = models.TextField(default='')
    tags = models.ManyToManyField(Tag)
    

    def __str__(self):
        return self.name
    
    def imageURL(self):
        try:
            img=self.project_photo.url
        except:
            img=''
        return img
    

class Testimonial(models.Model):
    testimonial_photo = models.ImageField(null=True, blank=True, default='default.jpg')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    testimonial_message = models.TextField()
    social_link_facebook = models.URLField(blank=True, null=True)
    social_link_twitter = models.URLField(blank=True, null=True)
    social_link_linkedin = models.URLField(blank=True, null=True)
    social_link_instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def imageURL(self):
        try:
            img=self. testimonial_photo.url
        except:
            img=''
        return img

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