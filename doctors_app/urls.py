# doctors_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctors_app.views import AccountViewset, SpecialtyViewset

router = DefaultRouter()
router.register(r'accounts', AccountViewset, basename='account')
router.register(r'specialties', SpecialtyViewset, basename='specialty')

urlpatterns = [
    path('', include(router.urls)),
]
