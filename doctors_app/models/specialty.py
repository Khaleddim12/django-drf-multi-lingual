from django.db import models
from django.utils.translation import gettext_lazy as _

class SpecialtyManager(models.Manager):
    use_for_related_fields = True

    AGE_RANGE = [
        ('All', _('All')),
        ('Adults', _('Adults')),
        ('Pediatric', _('Pediatric')),
        ('Neonatal', _('Neonatal')),
        ('Geriatric', _('Geriatric')),
    ]

    DIAGNOSTIC_THERAPEUTIC = [
        ('Diagnostic', _('Diagnostic')),
        ('Therapeutic', _('Therapeutic')),
        ('Both', _('Both')),
    ]

    SURGICAL_INTERNAL = [
        ('Internal', _('Internal')),
        ('Surgical', _('Surgical')),
        ('Both', _('Both')),
        ('Neither', _('Neither')),
    ]
    ORGAN_TECHNIQUE_BASED = [
        ('Organ', _('Organ')),
        ('Technique', _('Technique')),
        ('Both', _('Both')),
        ('Neither', _('Neither')),
        ('Multidisciplinary', _('Multidisciplinary')),
    ]
    
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset


class Speciality(models.Model):
    name = models.CharField(max_length=100, )
    
    age_range = models.CharField(max_length=10, choices=SpecialtyManager.AGE_RANGE, default='All')
    diagnostic_therapeutic = models.CharField(max_length=11, choices=SpecialtyManager.DIAGNOSTIC_THERAPEUTIC, default='Therapeutic')
    surgical_internal = models.CharField(max_length=10, choices=SpecialtyManager.SURGICAL_INTERNAL, default='Internal')
    organ_technique_based = models.CharField(max_length=18, choices=SpecialtyManager.ORGAN_TECHNIQUE_BASED, default='Organ')


    objects = SpecialtyManager()



    def __str__(self):
        return str(self.name_ar) + "\n" + str(self.name)

    def get_subSpecialities(self):
        return self.sub_speciality.all()
