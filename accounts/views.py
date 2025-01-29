from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import generics

def index(request):
    coffees = CoffeeMenu.objects.all()
    galleries = CoffeeGallery.objects.all()
    blogs = CoffeeBlog.objects.all()
    abouts = CoffeeAbout.objects.all()
    banners = CoffeeBanner.objects.all()
    topmenus = CoffeeTopMenu.objects.all()
    footer_info = Footer.objects.first()  
    reviews = Review.objects.all()
    socialMedia = SocialMedia.objects.all()
    for review in reviews:
        review.checked_stars = range(min(max(review.rating, 0), 5))  
        review.unchecked_stars = range(5 - min(max(review.rating, 0), 5))

    context = {
        'topmenus': topmenus,
        'banners': banners, 
        'abouts': abouts,
        'coffees': coffees,
        'galleries': galleries,
        'reviews': reviews,
        'blogs': blogs,
        'footer_info': footer_info,
        'SocialMedias' : socialMedia
    }

    return render(request, 'accounts/index.html', context)
