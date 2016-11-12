# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def Farmer(request):
	return render(request, 'Farmer/farmer.html')