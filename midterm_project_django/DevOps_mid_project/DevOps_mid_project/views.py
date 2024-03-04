from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Weight
from .modelForm import WeightForm
import templates 
import json


def home(request):
    weights = Weight.objects.all();
    form = WeightForm()
    if request.method == 'POST':
        Weight.objects.create(
            weight = request.POST.get('weight')
        )
        return redirect('/')
    context={'weights': weights, 'form':form}
    return render(request,"home.html",context)
