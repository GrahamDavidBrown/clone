from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from clone.models import City, User_Profile, Listing, Category, Sub_Category
from django.contrib.auth.models import User
from .forms import CityForm, RegistrationForm, NewListingForm
from django.contrib.auth import views as auth_views


def home(request):
    cities = City.objects.all()
    form = CityForm
    context = {'username': request.user.username, "id": request.user.id, "cities": cities, "form": form}
    return render(request, 'clone/city_pick.html', context)


def mylistings(request):
    cities = City.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            your_city = form.cleaned_data['your_city']
            your_city = City.objects.get(name=your_city)
            user_profile = User_Profile(user_id=request.user.id, city_id=your_city.id)
            user_profile.save()
            mylistings = Listing.objects.filter(owner_id=user_profile.user_id)
            context = {'mylistings': mylistings, 'name': request.user.username, 'city': your_city}
            return render(request, 'clone/mylistings.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CityForm()
        cities = City.objects.all()
    return render(request, 'clone/city_pick.html', {'username': request.user.username, "id": request.user.id, "cities": cities, "form": form})


def city_listings(request, city_id):
    profile = User_Profile.objects.get(user_id=request.user)
    city = City.objects.get(id=profile.city_id)
    city_listings = Listing.objects.filter(city=city)
    categories = Category.objects.filter()
    sub_cats = Sub_Category.objects.filter()
    context = {'categories': categories, 'sub_cats': sub_cats, 'city': city}
    return render(request, 'clone/city_listings.html', context)
    # return render(request, 'clone/city_listings.html', context)


def category_view(request, city_id, sub_cat):
    context = {'city': City.objects.get(name=city_id), 'sub_cat': Sub_Category.objects.get(name=sub_cat)}
    return render(request, 'clone/sub_cat_view.html', context)


def register(request):
    form = RegistrationForm
    context = {'form': form}
    return render(request, 'clone/register.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = username + "@stuff.stuff"
            user = User.objects.create_user(username=username, password=password, email=email, first_name='billy', last_name='goat', is_staff=True, is_superuser=True)
            user.save()
            context = {}
            return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        form = RegistrationForm
        context = {'form': form}
        return render(request, 'clone/register.html', context)


def new_listing(request, city_id, sub_cat):
    form = NewListingForm
    context = {'form': form, 'city': city_id, "sub_cat": sub_cat}
    return render(request, 'clone/new_listing.html', context)


def create_listing(request, city_id, sub_cat):
    if request.method == 'POST':
        form = NewListingForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            title = form.cleaned_data['title']
            picture_link = form.cleaned_data['picture_link']
            sub_cat = Sub_Category.objects.get(name=sub_cat).id
            city_id = City.objects.get(name=city_id).id
            owner_id = request.user.id
            listing = Listing(owner_id=owner_id, description=description, picture_link=picture_link, category_id=sub_cat, city_id=city_id, title=title)
            listing.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/")
        else:
            return HttpResponseRedirect("http://127.0.0.1:8000/")
