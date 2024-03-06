from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('adminP/', views.adminPage, name='adminP' ),
    path('about/', views.about, name='about' ),
    path('project/', views.projects, name='projects' ),
    path('testimonial/', views.testimonial, name='testimonial' ),
    path('skills/', views.skills, name='skill' )      

]