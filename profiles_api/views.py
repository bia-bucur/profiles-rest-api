from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """
        Test API view
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
            returns a list of APIView features
        """
        an_api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})

    def post(self, request):
        """
            Create a hello message with our name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'

            return Response({'message': message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, primary_key=None):
        """
            Handle updating an object

            Used to replace an object with the one the the request, and the primary_key is used to identify the object
        """
        return Response({"method": "PUT"})

    def patch(self, request, primary_key=None):
        """
            Handle a partial update of an object

            Used to update fields of an object, with the fields provided in the request
        """
        return Response({"method": "PATCH"})

    def delete(self, request, primary_key=None):
        """
            Delete an object
        """
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """
        Test API ViewSet
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
            Return a Hello message
        """
        a_viewset = [
            'Uses actions (list, create, retreive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """
            Create a new Hello message
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"

            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retreive(self, request, pk = None):
        """
            Handle getting an object by its ID
        """
        return Response({"http_method": "GET"})

    def update(self, request, pk = None):
        """
            Handle updating an object
        """
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk = None):
        """
            Handle updating part of an object
        """
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk = None):
        """
            Remove an object
        """
        return Response({"http_method": "DELETE"})
