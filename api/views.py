from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from api.models import ProjectDetail
from .serializers import ProjectDetailSerializer , UserSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

class getProjectDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        candidateData = ProjectDetail.objects.all()
        serialize = ProjectDetailSerializer(candidateData, many=True)
        return Response(serialize.data)

# class createProject(APIView):
#     # permission_classes = (IsAuthenticated,)
#     def post(self,request):

#         serialize = ProjectDetailSerializer(data=request.data)
        
#         if serialize.is_valid():
        
#             serialize.save()
            
#             return Response(serialize.data)

#         else:
        
#             return Response(serialize.errors)

# class searchProject(generics.ListAPIView):
    
#     queryset = ProjectDetail.objects.all()
    
#     serializer_class = ProjectDetailSerializer
    
#     filter_backends = [filters.SearchFilter]
    
#     search_fields = ['project_name']




class createProject(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProjectDetailSerializer
    queryset = ProjectDetail.objects.all()
    # def post(self,request):

    #     serialize = ProjectDetailSerializer
    #     queryset = ProjectDetail.objects.all()
    #     serialize.self.get_serializer(data = request.data)
    #     if serialize.is_valid():
    #         serialize.save()  
    #         return Response(serialize.data)
    #     else:
        
    #         return Response(serialize.errors)

class searchProject(generics.ListAPIView):
    
    queryset = ProjectDetail.objects.all()
    
    serializer_class = ProjectDetailSerializer
    
    filter_backends = [filters.SearchFilter]
    
    search_fields = ['project_name']





class Users(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):

        userData = User.objects.all()
        
        serialize = UserSerializer(userData, many=True)
        
        return Response(serialize.data)

class getNotification(APIView):
    def get(self, request):
        x = datetime.datetime.now()

        candidateData = ProjectDetail.objects.filter(project_duration_gte = x.month)
        serialize = ProjectDetailSerializer(candidateData, many = True)
        return Response(serialize.data)


class delete(APIView):
    def delete(self, request):
        User.objects.all().delete() 