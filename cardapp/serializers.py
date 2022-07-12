from rest_framework import serializers
from .models import user_info


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_info
        fields = '__all__'