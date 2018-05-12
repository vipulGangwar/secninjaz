from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test_form
from .serializers import *
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def test_form_collection(request):
    if request.method == 'GET':
        Test_form_data = Test_form.objects.all()
        serializer = Test_formSerializer(Test_form_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Test_formSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserList(generics.ListAPIView):
#     serializer_class = Test_formSerializer
#
#     def get_queryset(self):
#         print ("vipul")
#         email = self.kwargs['email']
#         print (email)
#         results = Test_form.objects.filter(email=email).values('first_name', 'last_name', 'email', 'password')
#         print (results)
#         if not results:
#             print ("NO")
#         else :
#             return results
#         return results


@api_view(['GET', 'POST'])
def test_user(request):
    if request.method == 'GET':
        Test_form_data = Test_form.objects.all()
        serializer = Validate_formSerializer(Test_form_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Validate_formSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            password = request.data['password']
            results = Test_form.objects.filter(email=email, password=password).values('first_name', 'last_name', 'email', 'password')
            if not results:
                return Response("error", status=status.HTTP_406_NOT_ACCEPTABLE)
            else :
                return Response(results, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
