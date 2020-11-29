from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , DetailView
from .models import Post

# Create your views here.

posts = [

	{
		'Name': 'Phillys',
		'Location': 'DHA sector Z',
		'Cuisines' : 'FASTfood',
		'Price Range' : '1',
		'Ratings' :'Very Good',

		
	},

	{

		'Name': 'Jammin Java',
		'Location':'LUMS',
		'Cuisines' : 'FASTfood',
		'Price Range' : '1',
		'Ratings' :'Very Good',
		
	}


]

def home(request):
	#context = {
	#	'restaurants': restaurants
	#}
	return render(request, 'blog/home.html') 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'}) 

def login(request):
	return render(request, 'blog/login.html', {'title': 'Login'})

def restaurants(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/restaurants.html', context)

def restaurants1(request):
	context1 = {
		'rests': Rest.objects.all()
	}
	return render(request, 'blog/tester.html', context1)

class PostListView(ListView):
	model=Post
	template_name='blog/restaurants.html'
	context_object_name='posts'
	paginate_by=7

class PostDetailView(DetailView):
	model=Post

