# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

def home(request):
	num = random.randint(0, 500)
	context = {
		"yeehonk": True, 
		"num": num,
	}
	return render(request, "home.html", context)

def home2(request):
	
	return render(request, "home2.html")

def home3(request):
	
	return render(request, "home3.html")

class ContactView(View):
	def get(self, request, *args, **kwargs):
		context = {
		"yeehonk": True,
		}
		return render(request, "home3.html", context)

class ContactTemplateView(TemplateView):
	template_name = "home3"
