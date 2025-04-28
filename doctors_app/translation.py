# doctors_app/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models.specialty import Speciality
from .models.account import Account

@register(Speciality)
class SpecialityTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Account)
class AccountTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'address_details', 'bio')
