from datetime import timedelta
from datetime import date
from ..models import *
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
            time_available = self.get_time_availabe(tache)
            tache.jour = date.today() + timedelta(days= round(time_available.days/2))


    def get_all_days(self):
        for i in self.__tache:
            if i.jour not in self.__liste_des_jour:
                self.__liste_des_jour.append(i.jour)
        return self.__liste_des_jour

    def get_days_task(self):
        for jour in self.__liste_des_jour:
            for tache in self.__tache:
                if tache.jour == jour:
                    if jour in self.__jour_tache.keys():
                        self.__jour_tache[jour].append(tache)
                    else:
                        self.__jour_tache[jour] =[]
                        self.__jour_tache[jour].append(tache)
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

    def __verify_all_workload(self):
        for charges in self.__charges.items():
            if charges[1] > self.__limite_time_task:
                return True
        return False

    def __verify_workload(self, jour):
        somme = 0
        for tache in self.__tache:
            if tache.jour == jour :
                somme += tache.duree_estimee
        return somme

    def __manage_workload(self):
        self.get_all_days()
        self.__workload_per_day()
        while self.__verify_all_workload():
            for charge in self.__charges.items():
                while self.__verify_workload(charge[0]):
                    for tache in self.__jour_tache[charge[0]]:
                        if (tache.jour + timedelta(days=1)) != tache.deadline.date():
                            tache.jour += timedelta(days=1)
                            tache.save()
                            break

    def get_task(self):
        self.__day_distribution()
        self.__manage_workload()
        return self.__tache

class