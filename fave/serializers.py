from django.db import IntegrityError
from rest_framework import serializers
from .models import Fave


class FaveSerializer(serializers.ModelSerializer):
    '''
    Fave serializer to convert Fave model into JSON,
    which can be displayed on frontend react app
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Fave
        fields = ['id', 'owner', 'caption', 'created_on']

    # Used CI Walkthrough Code
    def create(self, validated_data):
        '''
        If a user tries to Fave the same post more than once,
        it will raise an error message.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
