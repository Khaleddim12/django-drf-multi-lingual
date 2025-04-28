# serializers/account.py
from rest_framework import serializers
from doctors_app.models import Account, Speciality
from doctors_app.serializers.specialty import SpecialitySerializer

class AccountSerializer(serializers.ModelSerializer):
    specialities = SpecialitySerializer(required=False, read_only=True)
    speciality_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Speciality.objects.all(), required=False)
    
    address_en = serializers.CharField(required=False, write_only=True)
    address_ar = serializers.CharField(required=False, write_only=True)
    address_details_en = serializers.CharField(required=False, write_only=True)
    address_details_ar = serializers.CharField(required=False, write_only=True)
    bio_en = serializers.CharField(required=False, write_only=True)
    bio_ar = serializers.CharField(required=False)

    class Meta:
        model = Account
        fields = [
            'id', 
            'name',
            'name_en', 
            'name_ar', 
            'address',
            'address_en', 
            'address_ar', 
            'address_details', 
            'address_details_en', 
            'address_details_ar', 
            'bio', 
            'bio_en', 
            'bio_ar', 
            'specialities',
            'speciality_ids', 
            'is_verified', 
            'date_joined', 
            'last_updated'
        ]
        
        
    
    def create(self, validated_data):
        specialities_data = validated_data.pop('speciality_ids', [])
        account = Account.objects.create(**validated_data)
        if specialities_data:
            account.specialities.set(specialities_data)
        return account

    def update(self, instance, validated_data):
        specialities_data = validated_data.pop('speciality_ids', None)

        if specialities_data is not None:
            instance.specialities.set(specialities_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    