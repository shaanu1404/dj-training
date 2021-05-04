from django.shortcuts import render


def give_response(request):
    a = 3 + 5
    return render(request, 'products/index.html', {"a": a, "name": 'sysorex'})


def add_value(request):
    return render(request, 'products/about.html')
