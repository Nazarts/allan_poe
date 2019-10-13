from django.shortcuts import render


def home_view(request):
    context = {}
    return render(request, 'home.html', context)


def catalog_view(request):
    context = {}
    return render(request, 'reviews.html', context)


def single_view(request):
    context = {}
    return render(request, 'single.html', context)
