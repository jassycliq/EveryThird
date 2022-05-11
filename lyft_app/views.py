from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from lyft_app.serializers import TestSerializer


class Test(APIView):
    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            modifiedString = serializer.validated_data['string_to_cut'][2::3]
            return Response({"return_string": modifiedString}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
