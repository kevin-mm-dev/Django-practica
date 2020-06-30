
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializers



class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if(serializer.is_valid()):
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)