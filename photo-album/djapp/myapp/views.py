from django.shortcuts import render

# Create your views here.

# home page
def index(request):
    return render(request, 'frontend/photo/index.html')

# portfolio page
# def portfolio(request):
#     return render(request, 'frontend/photo/portfolio-detail.html')

# about page
# def about(request):
#     return render(request, 'frontend/photo/about.html')

