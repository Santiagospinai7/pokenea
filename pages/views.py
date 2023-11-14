from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Pokenea
from django import forms
from django.views import View
import os

# Create your views here.
class HomePageView(TemplateView):
  template_name = 'pages/home.html'

class PokeneaIndexView(TemplateView):
  template_name = 'pokeneas/index.html'
  def get(self, request):
    viewData = {}
    viewData['title'] = 'Pokenea Index'
    viewData['subtitle'] = 'All Pokeneas'
    viewData['pokeneas'] = Pokenea.objects.all()

    return render(request, self.template_name, viewData)
  
class PokeneaShowView(TemplateView):
  template_name = 'pokeneas/show.html'
  def get(self, request, pk):
    try:
      pokenea_id = int(pk)
      if (pokenea_id < 1):
        raise ValueError('Invalid Pokenea ID')
      get_object_or_404(Pokenea, pk=pokenea_id)
    except (ValueError, IndexError):
      return HttpResponseRedirect(reverse('home'))
    
    viewData = {}
    pokenea = Pokenea.objects.get(pk=pokenea_id)
    viewData['title'] = pokenea.name
    viewData['subtitle'] = 'Pokenea Detail'
    viewData['pokenea'] = pokenea
    viewData['container_id'] = os.uname()[1]

    return render(request, self.template_name, viewData)

class PokeneaForm(forms.ModelForm):
  class Meta:
    model = Pokenea
    fields = ['name', 'height', 'skill', 'image', 'phrase']

class PokeneaCreateView(View):
  print("PokeneaCreateView")
  template_name = 'pokeneas/create.html'

  def get(self, request):
    form = PokeneaForm()
    viewData = {}
    viewData["title"] = "Create pokenea"
    viewData["form"] = form
    return render(request, self.template_name, viewData)

  def post(self, request):
    form = PokeneaForm(request.POST)
    if form.is_valid(): 
      form.save()
      viewData = {
        "title": "Create pokenea", 
        "form": form, 
        "success_message": "Pokenea created"
        }
      return render(request, self.template_name, viewData)
    else:
      viewData = {}
      viewData["title"] = "Create pokenea"
      viewData["form"] = form
      return render(request, self.template_name, viewData)

