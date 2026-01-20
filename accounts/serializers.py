from rest_framework import serializers
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'account_type',
            'career_level',
            'interests',
            'profile_image',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
