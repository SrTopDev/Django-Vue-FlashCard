from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cardapp import views

urlpatterns = [
    path('user_info/', views.UserInfoList.as_view()),
    path('user_info/<int:pk>/', views.UserInfoDetail.as_view()),
    path('question_book/', views.QuestionBookList.as_view()),
    path('question_book/<int:pk>/', views.QuestionBookDetail.as_view()),
]