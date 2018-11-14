from django.contib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import

class UserViewSet(viewsets.ModeViewSet):
    """
    API endpoint that allows users to be viewd or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
