from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {
            "id": 5,
            "title": "To Kill A Mockingbird",
            "year": 1958,
        },
        {
            "id": 6,
            "title": "Constantine",
            "year": 2004,
        },
        {
            "id": 7,
            "title": "Matrix",
            "year": 1999,
        },
    ]
}


def movies(request):
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("Home page")
