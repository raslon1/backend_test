from rest_framework import serializers

from mobil_api.models import POS, Visit


class POSSerializer(serializers.ModelSerializer):
    class Meta:
        model = POS
        fields = ["pk", "pos_name"]


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ["pos", "date"]
