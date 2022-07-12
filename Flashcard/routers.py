from rest_framework import routers
from cardapp.viewsets import UserInfoViewSet

router = routers.DefaultRouter()
router.register(r'user_info', UserInfoViewSet)