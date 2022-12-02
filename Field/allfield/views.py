from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from . import module
from .form import FieldForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
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


class IndexAPI(APIView):
    def get(self, request):
        myData = module.serialize_form(FieldForm())
        return Response(data = myData, status=status.HTTP_200_OK)

    def post(self, request):
        form = FieldForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # form.save()
            return Response(data=form.errors, status=status.HTTP_200_OK)
        else:
             return Response(data=form.errors)


    