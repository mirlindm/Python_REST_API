from django.shortcuts import render


from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Category, Product
from . serializers import ProductSerializer, CategorySerializer

from rest_framework import status
from rest_framework.decorators import api_view


class welcome(APIView):

    def hello(self):

        return print("Welcome")
       

# @api_view(['GET', 'POST'])
# def product_list(request):
#     """
#     List all products, or create a new product
#     """

#     if request.method == "GET":
#         allProducts = Product.objects.all()
#         serializer = ProductSerializer(allProducts, many=True)
#         return Response(serializer.data)


#     elif request.method == "GET":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductList(APIView):
    """
    List all products or create a new product
    """

    def get(self, request, format=None):
        allProducts = Product.objects.all()
        serializer = ProductSerializer(allProducts, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryList(APIView):

    def get(self, request):
        allCategories = Category.objects.all()
        serializer = CategorySerializer(allCategories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetail(APIView):
    """
    Retrieve, update or delete a product instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product1 = self.get_object(pk)
        serializer = ProductSerializer(product1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product1 = self.get_object(pk)
        serializer = ProductSerializer(product1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product1 = self.get_object(pk)
        product1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryDetail(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category1 = self.get_object(pk)
        serializer = CategorySerializer(category1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category1 = self.get_object(pk)
        serializer = CategorySerializer(category1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category1 = self.get_object(pk)
        category1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
