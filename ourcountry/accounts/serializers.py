from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from country.models import *


class EmptySerializer(serializers.Serializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name',
                  'phone_number', 'birth_date')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def validate(self, data):
        # Проверяем, что пароли совпадают
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают.'})
        return data

    def create(self, validated_data):
        # Удаляем confirm_password перед созданием пользователя
        validated_data.pop('confirm_password')
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'first_name': instance.first_name,
                'email': instance.email,
                },
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Проверяем, что пароли совпадают
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают.'})

        # Аутентифицируем пользователя по email и паролю
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные или пользователь неактивен.')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'email': instance.email,
                'first_name': instance.first_name,
                'last_name': instance.last_name,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

#  RESET PASSWORD

class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email пользователя
    reset_code = serializers.IntegerField()  # 4-значный код
    new_password = serializers.CharField(write_only=True)  # Новый пароль

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        # Проверяем, существует ли указанный код для email
        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=reset_code)
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()
