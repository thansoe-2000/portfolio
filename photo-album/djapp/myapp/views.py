from django.shortcuts import render

# Create your views here.

# home page
def index(request):
    return render(request, 'frontend/photo/index.html')

# about page
def about(request):
    return render(request, 'frontend/photo/about.html')

# contact pages
def contact(request):
    return render(request, 'frontend/photo/contact.html')

# services pages
def services(request):
    return render(request, 'frontend/photo/services.html')

# gallary page
def gallary(request):
    return render(request, 'frontend/photo/gallary.html')

# gallary single page
def gallary_single(request):
    return render(request, 'frontend/photo/gallary-single.html')




