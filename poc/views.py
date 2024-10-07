from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def nested_example(request):
    return render(request, "nested_example.html")


def flat_example(request):
    return render(request, "flat_example.html")
