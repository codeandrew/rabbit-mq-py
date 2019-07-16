from rest_framework import viewsets, permissions
from .models import Items
from .serializers import ItemSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    
