from rest_framework import serializers
from mywebApp.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id',
        'email',
        'password',
        )