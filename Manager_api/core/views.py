from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None, mail_client=None, *args, **kwargs):
        if id:
            qs = User.objects.filter(id=int(id))
        elif mail_client:
            qs = User.objects.filter(email=mail_client)
        else:
            qs = User.objects.all()
        serializer = UserSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, id = None, *args, **kwargs):
        if id:
            user = User.objects.get(id=int(id))
            serializer = UserSerializer(instance=user,    data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

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

