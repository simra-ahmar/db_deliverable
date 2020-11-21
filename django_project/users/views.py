from django.shortcuts import render
from .models import customers
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
	if request.method == "POST":
		try:
			user = User.objects.get(username = request.POST['username'])
			return HttpResponse("Already taken")
		except User.DoesNotExist:
			user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
			phone = request.POST['contact']
			address = request.POST['address']
			newcustomer = customers(Contact = phone, Address = address, user = user )
			newcustomer.save()
			auth.login(request, user)
			return HttpResponse("Successful!")

			

	return render(request, 'blog/signup.html', {'title': 'Signup'})

@login_required(login_url = '/login/')
def showuserdata(request):
	datas = customers.objects.filter(user = request.user)
	return render(request, "blog/showdata.html", {'data' : datas})