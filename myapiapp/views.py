from django.contrib.auth.models import User
from django.http import Http404
from myapiapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapiapp.models import *

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):#all
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # permission_classes = [permissions.IsAuthenticated]
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except :
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EventList(APIView):
    """
    List all events, or create a new events.
    """
    def get(self, request, format=None):#all
        events = EventMaster.objects.all()
        serializer = EventSerializer(events, many=True)
        # permission_classes = [permissions.IsAuthenticated]
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class EventDetail(APIView):
    """
    Retrieve, update or delete a event instance.
    """
    def get_object(self, pk):
        try:
            return EventMaster.objects.get(pk=pk)
        except :
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = EventSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = EventSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all categories, or create a new categories.
    """
    def get(self, request, format=None):#all
        category = CategoryMaster.objects.all()
        serializer = CategorySerializer(category, many=True)
        # permission_classes = [permissions.IsAuthenticated]
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CategoryDetail(APIView):
    """
    Retrieve, update or delete a categorie instance.
    """
    def get_object(self, pk):
        try:
            return CategoryMaster.objects.get(pk=pk)
        except :
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = CategorySerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CategorySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShowEventOnCategoryDetails(APIView):
    """
    Retrieve, events based on category id instance.
    """

    def get(self, request, pk, format=None):
        events = EventMaster.objects.raw('SELECT * FROM myapiapp_eventmaster WHERE categoryName_id = %s', [pk])
        serializer = EventSerializer(events, many=True)
        permission_classes = [permissions.IsAuthenticated]
        return Response(serializer.data)


class TopEventOnCategoryDetails(APIView):
    """
    Retrieve, Category  based on  number of Events associated with category instance.
    """

    def get(self, request, format=None):
        events = CategoryMaster.objects.raw('select * from myapiapp_categorymaster where id in (SELECT  categoryName_id FROM myapiapp_eventmaster GROUP BY categoryName_id ORDER BY COUNT(id) DESC LIMIT 3)')
        serializer = CategorySerializer(events, many=True)
        permission_classes = [permissions.IsAuthenticated]
        return Response(serializer.data)
