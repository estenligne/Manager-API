from django.db import models
from django.contrib.auth.models import User



class relation_user(models.Model):
    user1 = models.ForeignKey(User, on_delete = models.CASCADE, related_name="receveur")
    user2 = models.ForeignKey(User, on_delete = models.CASCADE, related_name="demandeur")
    ami = models.BooleanField(default=False)


class Projet(models.Model):
    termine = "termine"
    en_cours = "en cours"
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    etat = models.CharField(
        max_length=200,
        choices= ((termine, "termine"), (en_cours, "en cours")),
        default=en_cours
    )
    def __str__(self):
        return self.nom



class Tache(models.Model):
    termine = "termine"
    en_cours = "en cours"
    nouveau = "nouveau"
    investigation = "investigation"
    besoin_de_clarification = "besoin de clarification"
    estimation = "estimation de temps"
    pres = "pres pour commencer"
    en_test = "en test"
    deployer = "deployer"
    completer = "completer"
    duplicate = "duplicate/double/repetition"
    fermer = "fermer"
    enquete_a_revoir = "enquete a revoir/ pas sure de la cause"


    basse = 'basse'
    moyenne = 'moyenne'
    elevee = 'elevee'
    critical= "critical/absolute"

    secondes = 'secondes'
    mins = 'mins'
    heures = 'heures'
    jours = 'jours'
    semaines = 'semaines'
    mois = 'mois'
    annees = 'annees'

    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null = True, blank = True)
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    user_asign = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asign', null=True, blank=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=200)
    priorite = models.CharField(
        max_length=17,
        choices=((basse ,'basse'),(moyenne , 'moyenne'),(elevee , 'elevee'), (critical, "critical/absolute")),
        default=basse,
    )
    duree_estimee = models.IntegerField( default=30)
    jour = models.DateField(null=True, default= None, blank=True)
    deadline = models.DateTimeField(null=True, default= None)
    etat = models.CharField(
        max_length=200,
        choices= (
            (termine, "termine"),
            (en_cours, "en cours"),
            (nouveau , "nouveau"),
            (investigation , "investigation"),
            (besoin_de_clarification , "besoin de clarification"),
            (estimation , "estimation de temps"),
            (pres , "pres pour commencer"),
            (en_test , "en test"),
            (deployer , "deployer"),
            (completer , "completer"),
            (duplicate , "duplicate/double/repetition"),
            (fermer , "fermer"),
            (enquete_a_revoir , "enquete a revoir/ pas sure de la cause")
        ),
        default=en_cours
    )
    fichier = models.FileField(null=True, blank=True)

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
    secondes = 'secondes'
    mins = 'mins'
    heures = 'heures'
    jours = 'jours'
    semaines = 'semaines'
    mois = 'mois'
    annees = 'annees'

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    date_attribution = models.DateField(auto_now_add=True)
    delais = models.IntegerField(null=True)
    unite_delais = models.CharField(
        max_length=8,
        choices=((secondes, 'secondes'),(mins, 'mins'),(heures, 'heures'),(jours, 'jours'),(semaines, 'semaines'),(mois, 'mois'),(annees, 'annees')),
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


