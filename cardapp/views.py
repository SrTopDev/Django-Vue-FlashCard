from django.shortcuts import render
from .models import user_info, question_book, setting
from .serializers import UserInfoSerializer, QuestionBookSerializer, SettingSerializer
from rest_framework import generics
import json

# Create your views here.
def vue_test(request):
    return render(request, 'cardapp/vue-test.html')


class UserInfoList(generics.ListCreateAPIView):
    serializer_class = UserInfoSerializer
    def get_queryset(self):
        name = self.request.query_params.get('user_id')
        password = self.request.query_params.get('password')
        queryset = user_info.objects.filter(user_id=name, password = password)
        return queryset
class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer
    def get_queryset(self):
        name = self.request.query_params.get('user_id')
        password = self.request.query_params.get('password')
        queryset = user_info.objects.filter(user_id=name, password = password)
        return queryset

class QuestionBookList(generics.ListCreateAPIView):
    serializer_class = QuestionBookSerializer
    queryset = question_book.objects.all()
class QuestionBookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionBookSerializer()
    queryset = question_book.objects.all()

class SettingList(generics.ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = setting.objects.all()
class SettingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SettingSerializer()
    queryset = setting.objects.all()



