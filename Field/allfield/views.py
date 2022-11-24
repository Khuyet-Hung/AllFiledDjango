from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import module
from .form import FieldForm
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class Index(View):
    def get(self, request):
        form = module.serialize_form(FieldForm())
        return render(request, 'demo.html', {'form': form})

    def post(self, request):
        form = FieldForm(request.POST, request.FILES)
        print (request.POST)
        if form.is_valid():
            return JsonResponse({"instance": form.errors})
        else:
             return JsonResponse({"error": form.errors})

    