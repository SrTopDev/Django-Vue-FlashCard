from rest_framework import serializers
from .models import user_info, question_book, setting


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_info
        fields = '__all__'
class QuestionBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_book
        fields = '__all__'
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = setting
        fields = '__all__'