from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from .models import Clothes
from .serializer import ClothesSerializer
from rest_framework.response import Response
# Create your views here.

class ClothesView(APIView):
    def get(self, request):
        output = [
            {
                'title':output.title
            } for output in Clothes.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    




def home(request):

    return render(request,'home.html')
