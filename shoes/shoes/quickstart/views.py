from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from shoes.quickstart import models, serializers

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer