from ..models import *
from ..MANAGER import Manager
from django.utils.deprecation import MiddlewareMixin

class DaysAttribution(MiddlewareMixin):

    def process_request(self, request):
        if 'taches' in request.META['PATH_INFO']:
            if request.META['REQUEST_METHOD'] == 'PUT' or request.META['REQUEST_METHOD'] == 'POST':
                print(f"l'utilisateur est {request.user}")
                qs = Tache.objects.filter(user = request.user.id, etat="en cours")
                manager = Manager(tache=qs)
                manager.apply_filters()
                print(f'ok pour le tri du user {request.user.id}')
                return None
            return None
        return None
