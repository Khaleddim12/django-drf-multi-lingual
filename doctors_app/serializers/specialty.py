from rest_framework import serializers
from doctors_app.models.specialty import Speciality

class SpecialitySerializer(serializers.ModelSerializer):
    name_en = serializers.CharField(required=True, write_only=True)
    name_ar = serializers.CharField(required=True, write_only=True)
    name = serializers.CharField(read_only=True)

    # Custom fields for translated choices
    age_range = serializers.SerializerMethodField(read_only=True)
    diagnostic_therapeutic = serializers.SerializerMethodField(read_only=True)
    surgical_internal = serializers.SerializerMethodField(read_only=True)
    organ_technique_based = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Speciality
        fields = [
            'id', 'name', 'name_en', 'name_ar',
            'age_range',
            'diagnostic_therapeutic',
            'surgical_internal', 
            'organ_technique_based'
        ]

    def get_age_range(self, obj):
        return obj.get_age_range_display()

    def get_diagnostic_therapeutic(self, obj):
        return obj.get_diagnostic_therapeutic_display()

    def get_surgical_internal(self, obj):
        return obj.get_surgical_internal_display()

    def get_organ_technique_based(self, obj):
        return obj.get_organ_technique_based_display()
