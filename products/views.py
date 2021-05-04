from django.shortcuts import render


def give_response(request):
    a = 3 + 5
    return render(request, 'products/index.html', {"a": a, "name": 'sysorex'})


def add_value(request):
    context = {
        "name": "sysorex",
        "age": 3
    }
    return render(request, 'products/about.html', context)
