import copy
import json
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def start (request):
    return HttpResponse("<h1> Hello </h1>")
