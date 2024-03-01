from django.shortcuts import render
from .forms import AboutForm, ProjectForm, TestimonialForm, SkillForm, ContactForm
from .models import About, Project, Testimonial, Skill, Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')


def posts(request):
    return render(request, 'posts.html')

def adminPage(request):
   
   return render(request, 'adminPage.html')


def about(request):
    about_form = AboutForm()
    skill_form = SkillForm()
    contact_form = ContactForm()
    return render(request, 'about.html', { 'about_form': about_form,
                                          'skill_form': skill_form,
                                          'contact_form': contact_form})

def projects(request):
    project_form = ProjectForm()
    return render(request, 'projects.html', { 'project_form': project_form})

def testimonial(request):
    testimonial_form = TestimonialForm()
    return render(request, 'testimonial.html', { 'testimonial_form': testimonial_form})

