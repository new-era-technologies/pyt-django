from django.http import HttpResponse, HttpRequest


def lesson1(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<p>Hello World!</p>')

def lesson11(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        '<p>Hello World!</p><p>Django є одним з найбільших framework на Python</p><hr>'
    )