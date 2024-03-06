from django import forms
from .models import About, Project, Testimonial, Skill, Contact

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_photo', 'name', 'project_link']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields =  "__all__"

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['number', 'email', 'github', 'instagram', 'linkedln', 'facebook']
