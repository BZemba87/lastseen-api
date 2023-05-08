from rest_framework import serializers
from .models import Caption
from love.models import Love
from fave.models import Fave


class CaptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    location = serializers.CharField()
    love_id = serializers.SerializerMethodField()
    fave_id = serializers.SerializerMethodField()
    love_count = serializers.ReadOnlyField()
    fave_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Pic must be smaller than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_love_id(self, obj):
        '''
        Logged in user can love the post and the love
        ID will be displayed in the post
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            love = Love.objects.filter(
                owner=user, caption=obj
            ).first()
            return love.id if love else None
        return None

    def get_fave_id(self, obj):
        '''
        Logged in user can Fave the post and the Fave
        ID will be displayed in the post
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            fave = Fave.objects.filter(
                owner=user,
                caption=obj
            ).first()
            if fave:
                return fave.id
            else:
                return None
        else:
            return None

    class Meta:
        model = Caption
        fields = [
            'id', 'owner', 'created_at', 'profile_id',
            'profile_image', 'title', 'content', 'location',
            'image', 'is_owner', 'love_id', 'fave_id',
            'love_count', 'fave_count'
        ]
