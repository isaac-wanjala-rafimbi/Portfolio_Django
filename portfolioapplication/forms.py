from django import forms
from .models import About, Project, Testimonial, Skill, Contact, Tag

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False, help_text='Enter tags separated by commas')
    class Meta:
        model = Project
        fields = ['project_photo', 'name', 'project_link', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['tags'].initial = ', '.join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if self.cleaned_data['tags']:
            tags = [tag.strip() for tag in self.cleaned_data['tags'].split(',')]
            instance.tags.set(*tags, clear=True)
        return instance

        


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
