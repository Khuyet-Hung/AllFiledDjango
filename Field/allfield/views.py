from django.shortcuts import render
from django.views import View
from . import module
from .form import FieldForm
from django.http import JsonResponse
import json

# Create your views here.
class Index(View):
    def get(self, request):
        form = module.serialize_form(FieldForm())
        return render(request, 'demo.html', {'form': form})

    def post(self, request):
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"instance": form.errors})
        else:
             return JsonResponse({"error": form.errors})

    