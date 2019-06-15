# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "second_app/index.html", context)

def josh(request):
    return HttpResponse("JOSH!!!")