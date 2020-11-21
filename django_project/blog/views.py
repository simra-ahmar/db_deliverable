from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [

	{
		'author': 'AdnanKhan',
		'title': 'Blog Post',
		'content': 'LUMSU Is Open',
		'date_posted': '11th November, 1111'
	},

	{
		'author': 'Ibrahim',
		'title': 'Blog Post 2',
		'content': 'Sab Marjayeinge, sirf Trivedi bachega',
		'date_posted': '69th November, 1969'
	}


]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context) 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'}) 

def login(request):
	return render(request, 'blog/login.html', {'title': 'Login'})

def restaurants(request):
	return render(request, 'blog/restaurants.html', {'title': 'Restaurants'})



