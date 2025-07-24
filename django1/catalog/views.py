from django.http import HttpResponse, HttpRequest


def catalog(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>THIS CATALOG PAGE</h1>')

def product(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>THIS PRODUCT PAGE</h1>')