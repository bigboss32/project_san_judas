from rest_framework.views import APIView
from rest_framework.response import Response

class ViewSales(APIView):
    def get(self, request, format=None):
        data = {'sales': [100, 200, 300, 400]}
        return Response(data)
