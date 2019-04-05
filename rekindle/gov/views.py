from django.shortcuts import render
from .forms import GovForm
from user.models import User1
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
def gov(request):
	form = GovForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	if not request.user.is_superuser:
		raise Http404	
	queryset = User1.objects.all()
	context= {
	"form":form,
	"object_list": queryset,
	}
	return render(request,"form2.html",context)

