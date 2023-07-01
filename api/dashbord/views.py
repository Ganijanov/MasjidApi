from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from main import models


@api_view(['GET'])
def list_masques(request):
    masques = models.Masque.objects.all()
    serializer = serializers.ListMasque(masques, many=True)
    return Response({'data': serializer.data})