from django.urls import path
from . import views


urlpatterns = [
    # frontend urls
    path('', views.index, name='index_page'),  #index_page
    path('about/', views.about, name='about_page'), # about page
    path('contact/', views.contact, name='contact_page'), #contact page
    path('services/', views.services, name='services_page'), #services page
    path('gallary/', views.gallary, name='gallary_page'), #gallary page
    path('gallary_single/', views.gallary_single, name='gallary_single_page'),  #gallary single page
    
 
    
]
