


from doctors_app.models import Account, Speciality
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from doctors_app.serializers.account import AccountSerializer

class AccountViewset(viewsets.ModelViewSet):
    
    queryset = Account.objects.prefetch_related(
        'specialities')
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

    
    