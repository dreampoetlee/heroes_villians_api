from this import s
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET'])
def super_types_list(request):

  if request.method == 'GET':
    super_type = SuperType.objects.all()
    serializer = SuperTypeSerializer(super_type, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    serializer = SuperTypeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def super_type_detail(request, pk):
  try:
    super_type = SuperType.objects.get(pk=pk)
    serializer = SuperTypeSerializer(super_type)
    return Response(serializer.data)
  except SuperType.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)



  print(pk)
  return Response(pk)