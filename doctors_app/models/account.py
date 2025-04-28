
from django.db import models
from django.utils.translation import gettext_lazy as _

from doctors_app.models.specialty import Speciality

class AccountManager(models.Manager):
    use_for_related_fields = True

    WEEKDAYS = [
        ("Saturday", _("Saturday")),
        ("Sunday", _("Sunday")),
        ("Monday", _("Monday")),
        ("Tuesday", _("Tuesday")),
        ("Wednesday", _("Wednesday")),
        ("Thursday", _("Thursday")),
        ("Friday", _("Friday")),
    ]

    OPENING_STATUS = [
        ("Unknown", _("Unknown")),
        # ("All-day-open", _("All-day-open")),
        # ("All-day-closed", _("All-day-closed")),
        # ("On-Shift", _("On-Shift")),
        # ("Two-Shifts", _("Two-Shifts")),
        ("Open", _("Open")),
        ("On-Call", _("On-Call")),
    ]

    OWNERSHIP = [
        
        ("Public", _("Public")),
        ("Private", _("Private")),
        ("Intersection", _("Intersection")),
        ("Other", _("Other")),

    ]

    ACCOUNT_TYPE = [
        ('Clinic', _('Clinic')), ('Hospital', _('Hospital')),
        ('Pharmacy', _('Pharmacy')), ('Lab', _('Lab')),  
        ('Insurance', _('Insurance')),  ('Company', _('Company')),
        ('Optical Center', _('Optical Center')), 
        ('Radiology Center', _('Radiology Center')), 
        ('Other', _('Other')),
        ('MLab', _('MLab')), 
        ('PALab', _('PALab')), 
        ('Pharmaceutical Companies', _('Pharmaceutical Companies')),
        ('Dental Compensation', _('Dental Compensation')), 
        ('Medical Center', _('Medical Center')),
    ]


class Account(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True) # validators=[validate_arabic]
    address = models.CharField(max_length=100, default= 'دمشق',) # validators=[validate_arabic]
    address_details = models.CharField(max_length=255, ) # validators=[validate_arabic_keywords]
    
    date_joined = models.DateField(verbose_name=_('Date joined'), auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)
    is_verified = models.BooleanField(default=False)
    specialities = models.ManyToManyField(Speciality, blank=True, related_name='account_specialities', db_index=True)
    bio = models.TextField(null=True, blank=True)
    