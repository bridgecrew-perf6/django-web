from django.shortcuts import render, redirect
from .forms import NewUserForm, HotelChainForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

# from django.views.generic import View, TemplateView, ListView, DetailView
from .models import HotelChain
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    # user = request.user
    print('homepage')
    # print(user.is_authenticated)
    # print(user.get_username)

    return render(request, "home.html", context={"user":{}})

def register_request(request):
    print('register request')
    form = NewUserForm()
    if request.method == "POST":
        print('print method post register:')
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "register successful!")
            return redirect("hotelpartner:homepage")

    return render(request, "register.html", context={"form":form})

def login_request(request):
    print('ssssss')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print('rrrr')
        if form.is_valid():
            print(form)
            # return redirect("hotelpartner:homepage")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("hotelpartner:homepage")
            else:
                print('yuyuykliiui')
                messages.error(request, "Invalid username or password.")
        else:
            print('error')
            print(request)
            messages.error(request, "Invalid username or password.")
    else:
        user = request.user
        if user.is_authenticated:
            return redirect("hotelpartner:homepage")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
    # return render(request, "login.html")
    # return render(request=request,"login.html")

def logout_request(request):
    logout(request)
    return redirect("hotelpartner:homepage")

@login_required
# @permission_required('polls.add_choice', raise_exception=True)
def create_hotel_chain(request):
    form = HotelChainForm()
    if request.method=="POST":
        form = HotelChainForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/hotelpartner/hotelchains")

    return render(request, "hotelchain/hotelchain_create.html", context={"hotel_chain_form": form})

def list_hotel_chain(request):
    hotelchains = HotelChain.objects.get_queryset().order_by('id')
    paginator = Paginator(hotelchains, 10)  # Show 25 contacts per page.
    page_number = 1
    if request.GET.get('page'):
        page_number = request.GET.get('page')
    page_hotel_chains = paginator.get_page(page_number)
    return render(request, "hotelchain/hotelchains.html", context={"hotel_chains": hotelchains, "page_hotel_chains": page_hotel_chains})

def detailhotelchain(request, pk = 0, slug = ''):
    print('pk'),
    print(pk)
    print(slug)
    detail_hotel_chain = HotelChain.objects.get(id=pk)
    print('detail')
    print(detail_hotel_chain.id)
    return render(request, "hotelchain/detailhotelchain.html", context={"detail_hotel_chain": detail_hotel_chain})

def edithotelchain(request, pk = 0, slug = ''):
    print('pk'),
    print(pk)
    print(slug)
    if request.method == "POST":
        hotel_chain_old = HotelChain.objects.get(id=pk)
        form = HotelChainForm(request.POST, instance=hotel_chain_old)
        print('ddd')
        if form.is_valid():
            form.save()

    detail_hotel_chain = HotelChain.objects.get(id=pk)
    print('detail')
    print(detail_hotel_chain.id)
    form = HotelChainForm(instance=detail_hotel_chain)
    return render(request, "hotelchain/hotelchain_edit.html", context={"detail_hotel_chain": detail_hotel_chain, "form": form })

def delete_hotel_chain(request):
    if request.method == "POST":
        pk = request.POST.get("pk", "0")
        print('pk')
        print(pk)
        if pk:
            d = HotelChain.objects.filter(id=pk).delete()


    return HttpResponseRedirect("/hotelpartner/hotelchains")
