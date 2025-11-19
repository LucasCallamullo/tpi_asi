from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def casos_uso(request):
    return render(request, 'home/casos_uso.html')


def alcances(request):
    return render(request, 'home/alcances_objetivo.html')



