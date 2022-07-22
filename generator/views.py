import random
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, "home.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    generatedpass=""
    if(request.GET.get("mayuscula")):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if(request.GET.get("especiales")):
        characters.extend("!#$%&/()=?¡¨*[]_><-{}´+¿'|°-+")
    if(request.GET.get("numeros")):
        characters.extend("123456789")
    for x in range(int(request.GET.get("length"))):
        generatedpass+=random.choice(characters)
    return render(request, "password.html", {"passw":generatedpass})