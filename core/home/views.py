from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])

def home(request):
    students_objs = Student.objects.all()
    serializer = StudentSerializer(students_objs, many=True)
    return Response({'status':200 , 'payload': serializer.data})



@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer= StudentSerializer(data=request.data)
  
    if not serializer.is_valid():
        print(serializer.errors) 
        return Response({'status': 403, 'errors' : serializer.errors , 'message':'Something went wrong'})
    serializer.save() 
    return Response({'status':200 ,  'payload': serializer.data, 'message':'you got data '})


@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer= StudentSerializer(student_obj, data=request.data)
  
        if not serializer.is_valid():
               print(serializer.errors) 
               return Response({'status': 403, 'errors' : serializer.errors , 'message':'Something went wrong'})
        serializer.save() 
        return Response({'status':200 ,  'payload': serializer.data, 'message':'you got data '})


    except Exception as e:
         return Response({'status':403, 'message':'invalid id'})

# Create your views here.
