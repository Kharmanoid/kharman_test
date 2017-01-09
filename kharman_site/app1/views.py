from django.shortcuts import render


def hello(request):
    print(request)
    return render(request, "hello.html", {})

def morning(request):
    print(request)
    return render(request, "morning.html", {})
