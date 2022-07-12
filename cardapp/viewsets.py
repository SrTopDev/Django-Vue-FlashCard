from .serializers import UserInfoSerializer
from rest_framework import viewsets
from .models import user_info

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = user_info.objects.all()
    serializer_class = UserInfoSerializer