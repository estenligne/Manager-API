from datetime import timedelta
from datetime import date
from math import *

class Manager:
    def __init__(self, tache=None, relation=None):
        self.__relations = relation
        self.__tache = tache.order_by('deadline')
        self.__liste_des_jour = []
        self.__charges = {}
        self.__jour_tache = {}
        self.__limite_time_task = 24

    def get_limite(self):
        return self.__limite_time_task

    def set_limite(self, limite):
        self.__limite_time_task = limite

    def get_time_availabe(self, queryset):
        return abs(date.today() - queryset.deadline.date())


    def __day_distribution(self):
        for tache in self.__tache :
            if (tache.jour - date.today()).days < 0:
                tache.jour = date.today()
            elif (tache.jour - tache.deadline.date()).days <0:
                pass
            else:
                time_available = self.get_time_availabe(tache)
                tache.jour = date.today() + timedelta(days= round(time_available.days/2))


    def get_all_days(self):
        self.__liste_des_jour.clear()
        for i in self.__tache:
            if i.jour not in self.__liste_des_jour:
                self.__liste_des_jour.append(i.jour)
        print(self.__liste_des_jour)
        return self.__liste_des_jour

    def get_days_task(self):
        self.__jour_tache.clear()
        for jour in self.__liste_des_jour:
            for tache in self.__tache:
                if tache.jour == jour:
                    if jour in self.__jour_tache.keys():
                        self.__jour_tache[jour].append(tache)
                    else:
                        self.__jour_tache[jour] =[]
                        self.__jour_tache[jour].append(tache)
        print(self.__jour_tache)
        return self.__jour_tache


    def get_charges(self):
        return self.__charges


    def __workload_per_day(self):
        self.__charges.clear()
        for tache in self.__tache:
            if tache.jour in self.__charges.keys():
                self.__charges[tache.jour] += tache.duree_estimee
            else:
                self.__charges[tache.jour] = tache.duree_estimee
        print(self.__charges)

    def __verify_all_workload(self):
        self.__workload_per_day()
        for charges in self.__charges.items():
            if charges[1] > self.__limite_time_task:
                return True
        return False

    def verify_workload(self, jour):
        somme = 0
        for tache in self.__tache:
            if tache.jour == jour :
                somme += tache.duree_estimee
        return somme


    def __manage_workload(self):
        self.get_all_days()
        self.__workload_per_day()
        self.get_days_task()
        while self.__verify_all_workload():
            for charge in self.__charges.items():
                print(charge)
                while self.verify_workload(charge[0]) > 24:
                    print(f"jour : {charge[0]} charge: {self.verify_workload(charge[0])}")
                    for tache in enumerate(self.__jour_tache[charge[0]]):
                        print(f"tache a decaler {tache}")
                        if (tache[1].jour + timedelta(days=1)) != (tache[1].deadline.date() +timedelta(days=1)):
                            tache[1].jour += timedelta(days=1)
                            tache[1].save()
                            print("decalage ok")
                            break
                    self.get_all_days()
                    self.get_days_task()


    def apply_filters(self):
        print("jours de depart")
        for i in self.__tache:
            print(i.jour)
        print("\ndistribution des jours")
        self.__day_distribution()
        print("\ngestions du nombres d'heures de taches par jours")
        self.__manage_workload()
        print("\njours choisis")
        for i in self.__tache:
            print(i.jour)
            i.save()


    def get_tasks(self):
        self.apply_filters()
        return self.__tache

