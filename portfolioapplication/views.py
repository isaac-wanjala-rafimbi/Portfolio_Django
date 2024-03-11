from django.shortcuts import redirect, render
from .forms import AboutForm, ProjectForm, TestimonialForm, SkillForm, ContactForm
from .models import About, Project, Testimonial, Skill, Contact

# Create your views here.
def home(request):
    about = About.objects.first()  
    contact = Contact.objects.first() 
    project_form = Project.objects.prefetch_related('tags').all()  # Fetch projects along with their tags
    testimonial= Testimonial.objects.all()

    return render(request, 'index.html', {'about': about, 'contact': contact, 'project_form': project_form,'testimonial': testimonial} )


def posts(request):
    return render(request, 'posts.html')

def adminPage(request):
    about = About.objects.first()  # Assuming there's only one about entry
    contact = Contact.objects.first()  # Assuming there's only one contact entry
    return render(request, 'adminPage.html', {'about': about, 'contact': contact})


def about(request):
    about_form = AboutForm()
    
    contact_form = ContactForm()
    if request.method == 'POST':
        about_form=AboutForm(request.POST, request.FILES)
        
        contact_form = ContactForm(request.POST)
        about_form.save()
        
        contact_form.save()
        return  redirect('adminP')
    return render(request, 'about.html', { 'about_form': about_form,
                                           'contact_form': contact_form})

def skills(request):
    skill_form = SkillForm()
    if request.method == 'POST':
        skill_form = SkillForm(request.POST)
        skill_form.save()
        
        return  redirect('adminP')

    return render(request, 'projects.html', { 'skill_form': skill_form})

def projects(request):
    project_form = ProjectForm()
    if request.method=='POST':
        project_form = ProjectForm(request.POST, request.FILES)
        project_form.save()

        return  redirect('adminP')
        

    return render(request, 'projects.html', { 'project_form': project_form})

def testimonial(request):
    testimonial_form = TestimonialForm()
    if request.method == 'POST':
        testimonial_form= TestimonialForm(request.POST)
        testimonial_form.save()        
        return  redirect('adminP')
    return render(request, 'testimonial.html', { 'testimonial_form': testimonial_form})

