from rest_framework import viewsets
from morgan.apps.identity import models
from morgan.api.v1.serializers.identity import IdentitySerializer


class Identity(viewsets.ModelViewSet):
    """
    List all identities
    """
    queryset = models.Identity.objects.all()
    serializer_class = IdentitySerializer

