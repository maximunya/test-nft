from rest_framework import serializers

from .models import Token


class TokenSerializer(serializers.ModelSerializer):
    '''Base token serializer'''
    class Meta:
        model = Token
        fields = '__all__'


class TokenCreateSerializer(serializers.ModelSerializer):
    '''Create token serializer'''

    def validate_owner(self, value):
        if not value.startswith('0x') or len(value) != 42:
            raise serializers.ValidationError('Invalid Ethereum address format.')
        return value

    class Meta:
        model = Token
        fields = ('media_url', 'owner')