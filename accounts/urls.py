from django.urls import path
from . import views
from .views import * 

urlpatterns = [
   path('', views.index),
   # path('generic/', views.generic),
   # path('elements/', views.elements),
   # path('about/', views.About, name='about'),  # About page
   # path('blog/', views.Blog, name='blog'),  # Blog page
   # path('reviews/', review_list, name='review_list'),  # Review page
   # path('coffee_list/', views.CoffeeList, name='coffee_list'),
   # path('footer/', footer_view, name='footer_view'),
]