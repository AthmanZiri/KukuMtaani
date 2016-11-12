from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from Farmer.models import farmer

urlpatterns=[
     url(r'^$', ListView.as_view(queryset=farmer.objects.all().order_by("-date")[:25], template_name="Farmer/all_farmers.html")),
     url(r'^(?P<pk>\d+)$', DetailView.as_view(model= farmer,template_name='Farmer/farmer.html'))
    ]