from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = (
            'id', 'email', 'username', 'date_created', 'date_modified',
            'firstname', 'lastname', 'password', 'confirm_password')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, user, validated_data):
        user.email = validated_data.get("email", user.email)
        user.username = validated_data.get("username", user.username)

        user.firstname = validated_data.get("firstname", user.firstname)
        user.lastname = validated_data.get("lastname", user.lastname)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        # confirm that password match the confirm password
        if password and password == confirm_password:
            user.set_password(password)

        user.save()
        return user

    def validate(self, data):
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.validationError("The password did not match")

        return data
