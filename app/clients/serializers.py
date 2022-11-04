from rest_framework import serializers
from .models import Client


class ClientsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone', 'login', 'name', 'birth', 'tg', 'email')


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Client
    #     fields = ('login', 'password')
    login = serializers.CharField(max_length=15, write_only=True)
    password = serializers.CharField(max_length=15, write_only=True)

    name = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        login = data.get('login', None)
        password = data.get('password', None)
        if login is None:
            raise serializers.ValidationError(
                'Неверно'
            )
        if password is None:
            raise serializers.ValidationError(
                'Неверно'
            )

        user = authenticate(username=login, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Пользователь не найден'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Пользователь деактивирован'
            )

        return {
            'token': user.token,
        }
