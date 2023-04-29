from rest_framework import serializers
from .models import Caption
from love.models import Love


class CaptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    love_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image must be smaller than 2MB!')
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
        user = self.context['request'].user
        if user.is_authenticated:
            love = Love.objects.filter(
                owner=user, Caption=obj
            ).first()
            return love.id if love else None
        return None

    class Meta:
        model = Caption()
        fields = [
            'id', 'owner', 'created_at', 'profile_id',
            'profile_image', 'title', 'content', 'image', 'is_owner',
            'love_id',
        ]
