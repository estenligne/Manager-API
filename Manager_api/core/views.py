from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from .serializer import *
from .models import *
from .MANAGER import *
import time
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserIdViewset(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, name=None, *args, **kwargs):
        return Response({'id': request.user.id})
class UserReViewset(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):

        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        return Response(user.save())

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
            return Response(serializer.data)



class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all().order_by('id')
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'put'], detail=True)
    def Tri(self, request):
        print("tri")
        print(request.data)
        qs = Tache.objects.filter(user=request.user.id, etat="en cours")
        manager = Manager(tache=qs)
        manager.apply_filters()
        print(f'ok pour le tri du user {request.user.id}')

class TacheUserViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        print(f"l'utilisateur est {request.user}")
        qs = Tache.objects.filter(user=request.user.id).order_by('id')
        serializer = TacheSerializer(qs, many=True, context={'request': request})
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



