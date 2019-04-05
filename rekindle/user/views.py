from django.shortcuts import render
from .forms import UserForm, LoginForm
from gov.models import Gov
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
def homepage(request):
	return render(request,"type.html")
def user(request):
	form = UserForm(request.POST or None)
	queryset = Gov.objects.all()

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context= {
	"form":form,
	"object_list": queryset,
	}
	return render(request,"form.html",context)
def about(request):
	return render(request,"about.html")
def login_page(request):
	form = LoginForm(request.POST or None)
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "auth/login.html", {})
def register_page(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "auth/register.html", {})