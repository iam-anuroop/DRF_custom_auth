from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import SessionAuthentication
from .permissions import Mypermission



class Student_view(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser

    authentication_classes = [SessionAuthentication]
    permission_classes = [Mypermission]
    

    

    
    


        


        




# Create your views here.
