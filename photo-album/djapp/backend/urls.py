from django.urls import path
from . import views

urlpatterns = [
    path('backend/', views.index, name='backend_page'),
]
