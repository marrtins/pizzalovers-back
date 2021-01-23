from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from .models import PizzaLover, Message
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .service import getPizzaLoversRank, notifyUsers


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaLoversView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.user.is_authenticated:
            pizzaLover = PizzaLover.objects.get_or_create(userID=request.user)[0]
            pizzaLover.vote()
            notifyUsers()
            return Response("Vote registered", status=status.HTTP_200_OK)
        else:
            return Response("Only authenticated users can vote", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        response = getPizzaLoversRank()
        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
