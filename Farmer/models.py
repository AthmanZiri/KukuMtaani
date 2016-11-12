# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class farmer(models.Model):
	full_name=models.CharField(max_length=200)
	mobile=models.CharField(max_length=13)
	location=models.CharField(max_length=255)
	produce=models.CharField(max_length=255)
	bio=models.TextField(max_length=500, null=True)
	date=models.DateTimeField()

	def __str__(self):
		return self.full_name