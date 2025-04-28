


from doctors_app.models import Speciality
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from doctors_app.serializers.specialty import SpecialitySerializer

class SpecialtyViewset(viewsets.ModelViewSet):
    
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = [AllowAny]

    
    