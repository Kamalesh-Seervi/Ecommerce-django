from django.urls import path

from playground import views


#Url conf default namesyntax
urlpatterns=[
    path('hello/',views.say_hello)
]