from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'email',
        ]

class ProjetSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'id',
            'nom',
            'type',
            'description',
            'etat',
            'user',
            'date_joined'
        ]

class TacheSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = [
            'id',
            'projet',
            'date_creation',
            'user',
            'user_asign',
            'nom',
            'description',
            'type',
            'priorite',
            'duree_estimee',
            'jour',
            'deadline',
            'etat',
            'fichier',
        ]

class Relation_tachesSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Relation_taches
        fields = [
            'id',
            'tache1',
            'tache2',
            'relation'
        ]

class EmployeSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = [
            'id',
            'user',
            'tache',
            'date_attribution',
            'delais',
            'unite_delais',
        ]

class Rapport_employeSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Rapport_employe
        fields = [
            'id',
            'employe',
            'date_creation',
            'date_choisie',
            'temps_choisi',
            'type_activite',
            'description',
        ]

class SuivreSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Suivre
        fields = [
            'id',
            'user',
            'tache',
            'autorisations',
        ]

class CommentairesSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = [
            'id',
            'user',
            'tache',
            'date_creation',
            'commentaire',
            'fichier',
        ]