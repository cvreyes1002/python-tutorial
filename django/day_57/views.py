from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

parameters = {
    "name": ""
}


def index(request, name):
    # Get age based on name
    parameters["name"] = name
    response = requests.get("https://api.agify.io", params=parameters)
    data = response.json()
    age = data["age"]

    # Get gender based on name
    response = requests.get("https://api.genderize.io", params=parameters)
    data = response.json()
    gender = data["gender"]

    return render(request, "day_57/index.html", {
        "name": parameters["name"],
        "age": age,
        "gender": gender,
    })
