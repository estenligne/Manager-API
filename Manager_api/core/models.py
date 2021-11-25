from django.db import models
from django.contrib.auth.models import User

class relation_user(models.Model):
    user1 = models.ForeignKey(User, on_delete = models.CASCADE, related_name="receveur")
    user2 = models.ForeignKey(User, on_delete = models.CASCADE, related_name="demandeur")
    ami = models.BooleanField(default=False)


class Projet(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    etat = models.CharField(max_length=200, default="en cours")
    def __str__(self):
        return self.nom


priority = (
    ('1', 'basse'),
    ('2', 'moyenne'),
    ('3', 'elevee'),
)
unite = (
    ("1", 'seconde'),
    ("2", 'min'),
    ("3", 'heure'),
    ("4", 'jour'),
    ("5", 'semaine'),
    ("6", 'mois'),
    ("7", 'annee'),
)
class Tache(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=200)
    priorite = models.CharField(
        max_length=7,
        choices=priority,
        default='basse',
    )
    duree_estimee = models.IntegerField()
    unite_duree = models.CharField(
        max_length=7,
        choices=unite,
        default='min'
    )
    jour = models.DateField(null=True, default= None)
    deadline = models.DateTimeField(null=True, default= None)
    etat = models.CharField(max_length=200)
    fichier = models.FileField(null=True)

    def __str__(self):
        return self.nom

# # c'est la premier qui est en relation avec la deuxieme
relation_tache = (
    ("1", 'depend de'),
    ("2", 'recquise pour'),
    ("3", 'avant'),
    ("4", 'apres'),
    ("5", 'en relation'),
)
class Relation_taches(models.Model):
    tache1 = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name='creator')
    tache2 = models.ForeignKey(Tache, on_delete=models.CASCADE)
    relation = models.CharField(
        max_length=13,
        choices = relation_tache,
        null = True
    )
    def __str__(self):
        return self.tache1.nom


class Employe(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    date_attribution = models.DateField(auto_now_add=True)
    delais = models.IntegerField(null=True)
    unite_delais = models.CharField(
        max_length=7,
        choices=unite,
        default='jour'
    )
    def __str__(self):
        return f"boss: '{self.tache.user.username}'\nemploye: '{self.user.username}'\ntache: '{self.tache.nom}' "

class Rapport_employe(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_choisie = models.DateField()
    temps_choisi = models.TimeField()
    type_activite = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"boss: '{self.employe.tache.user.username}'\nemploye: '{self.employe.user.username}'\ntache: '{self.employe.tache.nom}' "


class Suivre_rapport(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    autorisations = models.BooleanField(default=False)

    def __str__(self):
        return self.projet.nom

class Suivre(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    autorisations = models.BooleanField(default=False)

    def __str__(self):
        return self.tache.nom


class Commentaires(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField()
    fichier = models.FileField(null=True)

    def __str__(self):
        return f"{self.user.username}: '{self.tache.nom}'"


