from django.shortcuts import render

# Create your views here.


def edit(request,pk):
	return render(request, 'edit.html',{'pk':pk})


def view(request,pk):
	return render(request, 'view.html',{'pk':pk})

