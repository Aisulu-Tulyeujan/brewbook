from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from brewbookapp.models import User, Drink, Favorite, Ingredient
# Create your views here.

def index(request):        
    drinks = Drink.objects.all()
    return render(request, "brewbookapp/index.html", {
        "drinks": drinks,
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse()

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def favorites(request):
    pass

def register(request):
    if request.method == "POST":
        print("posted")
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "brewbookapp/register.html", {
                "message":"User already exists"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "brewbookapp/register.html")

def new_drink(request):
    if request.method == "POST":
        name = request.POST["name"]
        instruction = request.POST["instruction"]
        photo = request.FILES["photo"]
        video_url = request.POST.get("video_url")
        video_file = request.FILES.get("video_file")
        more_information = request.POST.get("more_information")
        drink = Drink(
            name = name,
            instruction =instruction,
            photo = photo,
            video_url = video_url,
            video = video_file,
            fun_facts = more_information
        )
        drink.save()
        for ingredient in request.POST["ingredients"].split(","):
            item = Ingredient(
                drink=drink,
                name=ingredient.strip()
            )
            item.save()
        return render(request, 'brewbookapp/new_drink.html', {
            "message": "Drink added."
        })
    else:
        return render(request, 'brewbookapp/new_drink.html')

def edit_drink(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    if request.method == "POST":
        drink.name = request.POST["name"]
        drink.instruction = request.POST["instruction"]
        if request.FILES.get("photo"):
            drink.photo = request.FILES.get("photo")
        if request.POST.get("video_url"):
            drink.video_url = request.POST.get("video_url")
        if request.FILES.get("video_file"):
            drink.video = request.FILES.get("video_file")
        drink.fun_facts = request.POST.get("more_information")
        drink.save()
        current_ingredients = set(Ingredient.objects.filter(drink=drink).values_list("name", flat=True))
        new_ingredients = set(name.strip() for name in request.POST["ingredients"].split(","))
        to_add = new_ingredients-current_ingredients
        to_delete = current_ingredients-new_ingredients
        Ingredient.objects.filter(drink=drink,name__in=to_delete).delete()
        for name in to_add:
            Ingredient.objects.create(drink=drink,name=name)
        return render(request, 'brewbookapp/new_drink.html', {
            "message": "Drink added."
        })
    else:
        return render(request, 'brewbookapp/new_drink.html', {
            "drink": drink
        })
    