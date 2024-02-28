from django import forms
from .models import About, Project, Testimonial, Skill, Contact

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['about_text', 'about_photo']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_photo', 'name', 'project_link', 'readmore_link']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial_photo', 'name', 'position', 'testimonial_message', 'social_link_facebook', 'social_link_twitter', 'social_link_linkedin', 'social_link_instagram']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['number', 'email', 'github', 'instagram', 'linkedln', 'facebook']
