from django.db import IntegrityError
from rest_framework import serializers
from love.models import Love


class LoveSerializer(serializers.ModelSerializer):
    """
    Serializer for the love model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Love
        fields = ['id', 'created_at', 'owner', 'caption']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
