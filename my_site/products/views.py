
from .models import Product, Category, File

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .seryalysers import *



#**********Product***********
class productlistAPIVIEW(APIView):

    def get(self, request):
        products=Product.objects.all()
        serialysers=poroductseryalysers(products, many=True, context={'request': request})
        return Response(serialysers.data)
    
    def post(self, request):
        serialyser=poroductseryalysers(data=request.data)
        if serialyser.is_valid():
            serialyser.save()
            return Response(serialyser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialyser.errors, status=status.HTTP_400_BAD_REQUEST)

class productdetailAPIVIEW(APIView):
    def get_pk(self,pk):
        try:
            product=Product.objects.get(pk=pk)
            return product
        
        except product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


    def get(self, request, pk):
        try:
            product=Product.objects.get(pk=pk)
            serialyser=poroductseryalysers(product)
            return Response(serialyser.data)
        
        except product.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            product=Product.objects.get(pk=pk)
            serialyser=poroductseryalysers(product, data=request.data)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
        if serialyser.is_valid():
            serialyser.save()
            return Response(serialyser.data)
        else:
            return Response(serialyser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        product=self.get_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#**********File***********

class filelistapiview(APIView):
    def get(self, request):
        file=File.objects.all()
        seryaliser=fileseryalysers(file, many=True, context={'request': request})
        return Response(seryaliser.data)
    
    def post(self, request):
        serializer=fileseryalysers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            serializer.errors

class filedetailapiview(APIView):
    def get(self,request, pk):
        try:
            file=File.objects.get(pk=pk)
            serialiser=fileseryalysers(file)
            return Response(serialiser.data)
        except file.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        



