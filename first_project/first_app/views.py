from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Hotel
from . import forms
# from first_app.forms import FormLogin, FormNewChain
# Create your views here.

def index(request):
    list_hotels = Hotel.objects.all();
    print(list_hotels)
    my_dict = {"data": list_hotels}
    #return HttpResponse('Hello World! 112333')
    return render(request, "first_app/index.html", context = my_dict)

def index2(request):
    my_dict = {"insert_me_2":"Thien xin chao ne 2223333!!!!!!"}
    return render(request, "first_app/index2.html", context = my_dict)

def login(request):
    form = forms.FormLogin()
    if request.method == "POST":
        form = forms.FormLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("username:" + form.cleaned_data['username'])
            print("password:" + form.cleaned_data['username'])
            print("note:" + form.cleaned_data['username'])
            print("botcatcher:" + form.cleaned_data['botcatcher'])

    data = {"form":form}
    return render(request, "first_app/form_login.html", context = data)

def newchain(request):
    form = forms.FormNewChain()
    if request.method == "POST":
        form = forms.FormNewChain(request.POST)
        print('sswww')
        if form.is_valid():
            print('forms')
            print(form)
            form.save(commit=True)
            index(request)
        else:
            print('Error save hotel chain')
    data = {"form": form}
    return render(request, "first_app/form_chain.html", context=data)