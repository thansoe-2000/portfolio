from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('portfolio/', views.portfolio, name='portfolio_page'),
    path('about/', views.about, name='about_page'),
]
