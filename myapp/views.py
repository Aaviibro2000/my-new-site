from django.http import HttpResponse


def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    return HttpResponse("<b>hello world</b>")

