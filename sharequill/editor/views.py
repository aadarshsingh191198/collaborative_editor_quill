from django.shortcuts import render

# Create your views here.
import requests

def edit(request,pk):
	requests.get('http://localhost:8080/api/edit/{}'.format(pk))
	return render(request, 'edit.html',{'pk':pk})


def view(request,pk):
	return render(request, 'view.html',{'pk':pk})

