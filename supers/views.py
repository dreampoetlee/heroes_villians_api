import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SupersSerializer
from .models import Supers


@api_view(['GET'])
def supers_list(request):

  super = Supers.objects.all()

  serializer = SupersSerializer(super, many=True)
  
  
  return Response(serializer.data)
  