from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from .serializer import *
from .models import *
import time

class Test_User_exist(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request, *args, **kwargs):
        return Response({'id':request.user.id})


class RegisterApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args,  **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            return Response({'statut': True})
        else:
            return Response({'statut': False})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserNameViewset(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, name=None, *args, **kwargs):
        if name:
            qs = User.objects.get(username = name)
            serializer = UserSerializer(qs, context={'request':request})
            return Response(serializer.data)
        else:
            return Response({'error': 'no email'})

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all().order_by('id')
    serializer_class = ProjetSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjetUserViewset(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
            qs= Projet.objects.filter(user= User.objects.get(id=request.user.id))
            serializer =ProjetSerializer(qs, many=True, context={'request': request})
            print(f"user : {request.user.id}")
            print(serializer.data)
            return Response(serializer.data)



class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all().order_by('id')
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]


class TacheUserViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        qs = Tache.objects.filter(user=User.objects.get(id=request.user.id))
        serializer = TacheSerializer(qs, many=True, context={'request': request})
        print(f"user : {request.user.id}")
        return Response(serializer.data)

class Relation_TachesViewSet(viewsets.ModelViewSet):
    queryset = Relation_taches.objects.all().order_by('id')
    serializer_class = Relation_tachesSerializer        
    permission_classes = [permissions.IsAuthenticated]

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all().order_by('id')
    serializer_class = EmployeSerializer
    permission_classes = [permissions.IsAuthenticated]

class Rapport_employeViewSet(viewsets.ModelViewSet):
    queryset = Rapport_employe.objects.all().order_by("id")
    serializer_class = Rapport_employeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SuivreViewSet(viewsets.ModelViewSet):
    queryset = Suivre.objects.all().order_by("id")
    serializer_class = SuivreSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentairesViewSet(viewsets.ModelViewSet):
    queryset = Commentaires.objects.all().order_by("id")
    serializer_class = CommentairesSerializer
    permission_classes = [permissions.IsAuthenticated]

