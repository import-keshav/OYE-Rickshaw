from rest_framework import serializers

from . import models

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TODO
        fields = '__all__'
