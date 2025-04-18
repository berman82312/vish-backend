from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
