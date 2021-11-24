from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all().order_by('id')
    serializer_class = ProjetSerializer
    permission_classes = [permissions.IsAuthenticated]

class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all().order_by('id')
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]

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

